from django.shortcuts import render,redirect
from django.http import JsonResponse 
from django.template.loader import render_to_string 
from django.views.generic import ListView,DetailView
from django.views.decorators.cache import cache_page
from .models import *
from django.db.models import Q , F
from django.db.models import Count, Sum, Avg, Max, Min
from .tasks import send_emails
class ProductList(ListView):
    model = Product
    paginate_by =30
    
class ProductDetail(DetailView):
    model = Product
    queryset = Product.objects.annotate(no_reviews=Count('product_review'))
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
    paginate_by=20
    
  

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
    
@cache_page(60*1)
def debug(request):
    send_emails.delay()
    return render(request,'debug.html',{'debug':Product.objects.all()})

def add_review(request,slug):
    rate=request.POST.get("rate")
    review=request.POST.get("review")
    product=Product.objects.get(slug=slug)
    
    Review.objects.create(
        user=request.user,
        rate=rate,
        review=review,
        product=product 
    )
    reviews = Review.objects.filter(product=product)
    html = render_to_string('include/add_review_include.html',{'reviews':reviews})
    return JsonResponse({'result':html})