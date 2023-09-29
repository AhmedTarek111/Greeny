from django.shortcuts import render
from .models import *
from django.views.generic import ListView

class OrderList(ListView):
    model = Order
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    