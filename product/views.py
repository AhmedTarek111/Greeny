from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
from django.db.models import Q , F
from django.db.models import Count, Sum, Avg, Max, Min

class ProductList(ListView):
    model = Product
    
    
class ProductDetail(DetailView):
    model = Product
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["images"] = ProductImages.objects.filter(product_id=product.id)
        context["reviews"] = Review.objects.filter(product_id=product.id)
        context["related_name"] = Product.objects.filter(brand=self.get_object().brand)
        
        return context
    
class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(avg_rate=Count('brand_product'))

class BrandDetail(ListView): # we use list view in this situation beacause the pagination is supported by default in the list view and beacause it not exist in the detail view
    model = Product
    context_object_name = 'products_of_brand'
    template_name = 'product/brand_detail.html'

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    

class Debug(ListView):
    model =Product 
    template_name ='product/debug.html'
    queryset = Product.objects.distinct()


    