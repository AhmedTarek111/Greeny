from django_filters import rest_framework as filters
from .models import Product

class ProudctFillter(filters.FilterSet):
    class Meta:
        model= Product
        fields = {
            'name' : ['contains'],
            'price' : ['range','gte','lte'],
        }