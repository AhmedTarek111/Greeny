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
    path('api/<str:username>/<int:pk>',OrderDetailAPI.as_view()),
    path('api/<str:username>/create_order',CreateOrderAPI.as_view()),
    path('api/<str:username>/apply_coupon',ApplyCouponAPI.as_view()),
    # payment
    path('checkout/payment/',create_checkout_session),
    path('checkout/payment/success/',payment_success),
    path('checkout/payment/failed/',payment_failed),

]