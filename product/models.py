from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models import Count, Sum, Avg, Max, Min


class Product(models.Model):
    FLAG_CHOICES=(
        ('Sale','Sale'),
        ('New','New'),
        ('Feature','Feature'),
    )

    name = models.CharField(verbose_name=_('Name'),max_length=50)
    subtitle=models.CharField(verbose_name=_('Subtitle'),max_length=50)
    image = models.ImageField(verbose_name=_('Image'),upload_to='products')
    price = models.FloatField(verbose_name=_('Price'))
    sku = models.CharField(verbose_name=_('SKU'),max_length=150)
    description = models.TextField(verbose_name=_('Description'),max_length=40000)
    flag = models.CharField(verbose_name=_('Flag'),max_length=50,choices=FLAG_CHOICES)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),on_delete=models.SET_NULL,null=True, related_name='brand_product')
    quantity = models.IntegerField(default=0)
    tags = TaggableManager()
    slug = models.SlugField(null=True ,blank=True)

    
    def __str__(self):
        return self.name
   
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Product, self).save(*args, **kwargs) 

    def avg_rate(self):
        avg = self.product_review.aggregate(rate_avg=Avg('rate'))
        rate_avg = avg['rate_avg']
        if rate_avg is not None:
            result = round(rate_avg, 1)
            return result
        else:
            return 0.0 

    
class ProductImages(models.Model):
    product= models.ForeignKey(Product,verbose_name=_("product"),on_delete=models.CASCADE,related_name='products_images')
    image = models.ImageField(verbose_name=_("Image"),upload_to='product_images')
    def __str__(self):
        return str(self.product)
    
class Brand(models.Model):
    name=models.CharField(verbose_name=_("Name"),max_length=50)
    image = models.ImageField(verbose_name=_("Image"),upload_to='brand_images') 
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug =slugify(self.name)
       super(Brand, self).save(*args, **kwargs) 


class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_("User"),on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,verbose_name=_("Product"),on_delete=models.CASCADE,related_name='product_review')
    review = models.TextField(verbose_name=_("Review"),max_length=500)
    rate = models.IntegerField(verbose_name=_("Rate"))
    date = models.DateTimeField(verbose_name=_("Date"),default=timezone.now)
    def __str__(self):
        return f"{str(self.product)} -> {self.review}"
    
