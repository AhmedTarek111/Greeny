from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("products/",ProductList.as_view()),
    path("products/<int:pk>/",ProductDetail.as_view()),
]

