from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import JsonResponse 
from django.template.loader import render_to_string 
from .models import Deleviry_fee
class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginate_by =3
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@login_required
def order_checkout(request):
    cart = Cart.objects.get(user=request.user,status='In Progress')
    cart_detail =CartDetail.objects.filter(cart=cart)
    delivery_fee = Deleviry_fee.objects.last().fee
    discount_value=0
    if request.method == 'POST':
        coupon = Coupon.objects.get(code=request.POST['code'])
        if coupon and coupon.quantity > 0:
                now_date_time = datetime.datetime.today().date()  
                if coupon and coupon.start_date.date() <= now_date_time <= coupon.end_date.date():
                        discount_value = cart.cart_total() * coupon.discount / 100
                        total_cart = cart.cart_total() - discount_value
                        cart.total_after_coupon = total_cart
                        coupon.quantity -= 1
                        coupon.save()
                        cart.coupon = coupon
                        cart.save()
                        total = round(delivery_fee + total_cart,2)
                        
                        html = render_to_string('include/apply_coupon_include.html',{
                            'cart_detail': cart_detail,
                            'sub_total': cart.cart_total,
                            'cart_total': total,
                            'coupon': discount_value,
                            'delivery_fee': delivery_fee,
                        })
                        return JsonResponse({'result':html})
    else:
                       
        total_cart = cart.cart_total()
        total = delivery_fee + total_cart

    return render(request, 'orders/checkout.html', {
            'cart_detail': cart_detail,
            'sub_total': total_cart,
            'cart_total': total,
            'coupon': discount_value,
            'delivery_fee': delivery_fee,
    })

def add_to_cart(request):
    cart = Cart.objects.get(user=request.user, status='In Progress')
    quantity = int(request.POST['quantity'])
    product = Product.objects.get(id=request.POST['products'])
    price = product.price

    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, products=product, defaults={
        'quantity': quantity,
        'total': round(price * quantity, 2),
        'price': price,
    })

    if not created:
        cart_detail.quantity += quantity
        cart_detail.total = round(cart_detail.price * cart_detail.quantity, 2)
        cart_detail.save()
    return redirect(f"/products/{product.slug}/")

def remove_from_cart(request):
    id= request.POST['id']
    cart_detail=CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect(f"/products/")