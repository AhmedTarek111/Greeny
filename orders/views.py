from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin






class OrderList(LoginRequiredMixin,ListView):
    model = Order
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