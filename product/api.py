from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Product ,Brand
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView



class product_list_API(ListAPIView):
    queryset = Product.objects.all()    
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'subtitle','description',]
class CreateUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()   
    serializer_class = ProductDetailSerializers

class BrandListAPI(ListAPIView):
    queryset =Brand.objects.all()
    serializer_class = BrandListSeralizers

class BrandDetailAPI(RetrieveAPIView):
    queryset =Brand.objects.all()
    
    serializer_class = BrandDetailSeralizers