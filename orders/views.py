from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin






class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginate_by =3
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@login_required
def order_checkout(request):
    cart = Cart.objects.get(user=request.user,status='In Progress')
    cart_detail =CartDetail.objects.filter(cart=cart)
    context ={
        'cart_detail':cart_detail
    }
    return render(request ,'orders/checkout.html',context)

def add_to_cart(request):
    cart=Cart.objects.get(user=request.user,status='In Progress')
    quantity=int(request.POST['quantity'])
    product= Product.objects.get(id=request.POST['products'])
    cart_detail=CartDetail.objects.get_or_create(cart=cart ,products=product,quantity=quantity,total=round(int(product.price) * quantity,2))
    return redirect(f"/products/{product.slug}/")

def remove_from_cart(request):
    id= request.POST['id']
    cart_detail=CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect(f"/products/")