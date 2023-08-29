from django.contrib import admin
from .models import Product,ProductImages,Brand,Review
# Register your models here.
class ImageProductInline(admin.TabularInline):
    model = ProductImages
class  ProductAdmin(admin.ModelAdmin):
    list_display = ['name','subtitle','image','price','flag','brand','description']
    list_filter = ['name','subtitle','brand','description']
    search_fields = ['name','subtitle','description']
    inlines =[ImageProductInline,]
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)