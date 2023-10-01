from django.urls import path ,include
from .views import *

app_name='orders'

urlpatterns = [
    path('',OrderList.as_view()),
    path('checkout/',order_checkout,name='checkout'),
    path('add_to_cart/',add_to_cart,name='add_to_cart')
]