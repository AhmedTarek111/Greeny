from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product
from rest_framework.generics import ListAPIView



class product_list_api(ListAPIView):
    queryset = Product.objects.all()    
    serializer_class = ProductSerializers

class product_detail_api(ListAPIView):
    queryset = Product.objects.all()   
    serializer_class = ProductSerializers
    
