from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from .serializers import *
from .models import Product ,Brand
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .myfilter import ProudctFillter
from .myPagination import MyPagination


class product_list_API(ListAPIView):
    queryset = Product.objects.all()    
    serializer_class = ProductListSerializers
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['name','price']
    ordering_fields = ['name', 'price']
    filterset_class =ProudctFillter
    pagination_class =MyPagination
class CreateUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()   
    serializer_class = ProductDetailSerializers

class BrandListAPI(ListAPIView):
    queryset =Brand.objects.all()
    serializer_class = BrandListSeralizers

class BrandDetailAPI(RetrieveAPIView):
    queryset =Brand.objects.all()
    serializer_class = BrandDetailSeralizers