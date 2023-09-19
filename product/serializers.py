from rest_framework import serializers
from .models import Product , Brand ,Review
from django.db.models import Count,Avg
from django.db.models.functions import Coalesce
from django.db.models.functions import Round  
from taggit.serializers import (TagListSerializerField,TaggitSerializer)

class ProductListSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    avg_rate=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        rate_avg = avg['rate_avg']
        if rate_avg is not None:
            result = round(rate_avg, 1)
            return result
        else:
            return 0.0 

  

class ProductDetailSerializers(serializers.ModelSerializer,TaggitSerializer,):
    avg_rate=serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
            avg = product.product_review.aggregate(rate_avg=Avg('rate'))
            rate_avg = avg['rate_avg']
            if rate_avg is not None:
                result = round(rate_avg, 1)
                return result
            else:
                return 0.0 

class BrandListSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSeralizers(serializers.ModelSerializer):
    products=ProductListSerializers(source='brand_product',many=True)
    class Meta:
        model = Brand
        fields ='__all__'
