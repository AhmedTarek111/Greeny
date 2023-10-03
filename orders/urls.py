from django.urls import path ,include
from .views import *
from .api import *
app_name='orders'

urlpatterns = [
    path('',OrderList.as_view()),
    path('checkout/',order_checkout,name='checkout'),
    path('add_to_cart/',add_to_cart,name='add_to_cart'),
    path('delete_from_cart/',remove_from_cart,name='delete'),
    # API
    path('api/<str:username>/cart/',CartAPI.as_view()),
    path('api/<str:username>/cart/delete',CartAPI.as_view()),
    path('api/<str:username>/list',OrderListAPI.as_view()),
]