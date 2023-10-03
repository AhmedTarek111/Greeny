from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveAPIView
from rest_framework.response import Response

class CartAPI(GenericAPIView):
    def get(self,request,*args, **kwargs):
        cart,created =Cart.objects.get_or_create(user=User.objects.get(username=self.kwargs['username']), status='In Progress')
        data= CartSerializers(cart).data
        return Response(data)
    
    def post(self,request,*args, **kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        cart =Cart.objects.get(user=user, status='In Progress')
        product=Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data.get('quantity'))
        cart_detail,created=CartDetail.objects.get_or_create(cart=cart,products=product )
        cart_detail.total=round(product.price * quantity,2)
        cart_detail.quantity=quantity
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