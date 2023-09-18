from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api import *
urlpatterns = [
    path("products/",ProductList.as_view()),
    path("products/<slug:slug>/",ProductDetail.as_view()),
    path("Brands/",BrandList.as_view()),
    path("Brands/<slug:slug>/",BrandDetail.as_view()),
    path("debug/",Debug.as_view()),
    path('api/list/',product_list_api),
    path('api/list/<int:pk>',product_detail_api),

]

