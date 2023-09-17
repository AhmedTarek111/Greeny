from django.shortcuts import render
from product.models import Product,Brand,Review
from django.db.models import Count,Avg
from django.db.models.functions import Round  
from django.db.models.functions import Coalesce
def home(request):
    
    context={
        'brands':Brand.objects.distinct()[:10].annotate(brands_count=Count('brand_product')),
        'sold_products': Product.objects.filter(flag='Sale')[:10].annotate(a_r=Round(Avg('product_review__rate'),1)),
        'feature_products': Product.objects.filter(flag='Feature')[:6].annotate(a_r=Round(Coalesce('product_review__rate',0),1)),
        'new_products': Product.objects.filter(flag='New')[:10].annotate(a_r=Round(Coalesce('product_review__rate',0),1)),
        'reviews':Review.objects.all()[:4]
    }
    return render( request,'settings/home.html',context)