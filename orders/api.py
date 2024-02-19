from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import User

class CartAPI(GenericAPIView):
    def get(self,request,*args, **kwargs):
        cart,created =Cart.objects.get_or_create(user=User.objects.get(username=self.kwargs['username']), status='In Progress')
        data= CartSerializers(cart).data
        return Response(data)
    
    def post(self,request,*args, **kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        cart =Cart.objects.get(user=user, status='In Progress')
        product=Product.objects.get(id=request.data.get('product_id'))
        quantity = int(request.data.get('quantity'))
        price = product.price
        cart_detail, created = CartDetail.objects.get_or_create(cart=cart, products=product, defaults={
                'quantity': quantity,
                'total': round(price * quantity, 2),
                'price': price,
            })
        if created:                 
            cart_detail.total=round(product.price * quantity,2)
            cart_detail.quantity=quantity
        else:
            cart_detail.quantity +=1
            
        cart_detail.save()
        cart =Cart.objects.get(user=user, status='In Progress')
        data =CartSerializers(cart).data
        return Response({'message':'product added successfully' , 'data':data})
        

    def delete(self,request,*args, **kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        cart =Cart.objects.get(user=user, status='In Progress')
        product=Product.objects.get(id=request.data['product_id'])
        cart_detail=CartDetail.objects.get(cart=cart,products=product)
        cart_detail.delete()

        cart =Cart.objects.get(user=user, status='In Progress')
        data = CartSerializers(cart).data

        return Response({
            "message":"cart detail deleted successfully",
            'data':data,
        })


class OrderListAPI(ListAPIView):
        model = Order
        queryset =Order.objects.all()
        
        def list(self,*args, **kwargs):
             user =User.objects.get(username=self.kwargs["username"])
             order= self.queryset.filter(user=user  )
             data = OrderListSerializers(order,many=True).data
             return Response(data)

class OrderDetailAPI(RetrieveAPIView):
     serializer_class = OrderListSerializers
     queryset = Order.objects.all()


class CreateOrderAPI(GenericAPIView):
     
    def get(self,*args, **kwargs):
        #   cart -> order
        #   cart detail -> order detail 

        user =User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user ,  status='In Progress')

        new_order =Order.objects.create(
             user =user,
             status = 'Order Recieved',
             coupon =cart.coupon,
             total_after_coupon =cart.total_after_coupon,
        )

        cart_detail=CartDetail.objects.filter(cart=cart)
        for object in cart_detail:
                OrderDetail.objects.create(
                    order=new_order,
                    products = object.products,
                    quantity = object.quantity,
                    price = object.price,
                    total=round(int(object.products.price) * object.quantity,2)

                    
                               
                )
        cart.status ='Completed'
        cart.save()

        return Response({
             'message':'the order has been created',

             }
             )

class ApplyCouponAPI(GenericAPIView):

     def post(self,request,*args, **kwargs):
        user =User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='In Progress')
        coupon = Coupon.objects.get(code=request.data['code'])
        if coupon and coupon.quantity > 0:
                now_date_time = datetime.datetime.today().date()  # Corrected the method call
                if now_date_time >= coupon.start_date.date() and now_date_time <= coupon.end_date.date():
                    discount_value = cart.cart_total() * coupon.discount / 100
                    total_cart = cart.cart_total() - discount_value
                    cart.total_after_coupon = total_cart
                    coupon.quantity -= 1
                    coupon.save()
                    cart.coupon = coupon
                    cart.save()
                    return Response({ 'message' : 'the coupon has been applied successfully '})
                else:
                    return Response({'message':'the coupon time not valid'})
        else:
                return Response({'message':'the coupon not valid'})
