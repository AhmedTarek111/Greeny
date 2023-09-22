from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api import *




urlpatterns = [
    path("products/",ProductList.as_view()),
    path("products/<slug:slug>/",ProductDetail.as_view()),
    path("brands/",BrandList.as_view()),
    path("brands/<slug:slug>/",BrandDetail.as_view()),
    path("debug/",Debug.as_view()),
                    # API
    path('api/products/',product_list_API.as_view()),
    path('api/products/<int:pk>/',CreateUpdateDelete.as_view()),
    path('api/brands/', BrandListAPI.as_view() ),
    path('api/brands/<int:pk>/',BrandDetailAPI.as_view()),
    
]

