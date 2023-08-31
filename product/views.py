from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *

class ProductList(ListView):
    model = Product
    
    
class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["images"] = ProductImages.objects.filter(product_id=product.id)
        context["reviews"] = Review.objects.filter(product_id=product.id)
        return context
    