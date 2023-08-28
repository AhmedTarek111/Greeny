from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    FLAG_CHOCICES=(
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
    flag = models.CharField(verbose_name=_('Flag'),max_length=50,choices=FLAG_CHOCICES)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    image = models.ImageField(verbose_name=_("Image"),upload_to='proudct_images')
    proudct= models.ForeignKey(Product,verbose_name=_("Proudct"),on_delete=models.CASCADE)
    def __str__(self):
        return str(self.proudct)
    
class Brand(models.Model):
    name=models.CharField(verbose_name=_("Name"),max_length=50)
    image = models.ImageField(verbose_name=_("Image"),upload_to='brand_images') 
    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_("User"),on_delete=models.SET_NULL,null=True)
    proudct = models.ForeignKey(Product,verbose_name=_("Proudct"),on_delete=models.CASCADE)
    review = models.TextField(verbose_name=_("Review"),max_length=500)
    rate = models.IntegerField(verbose_name=_("Rate"),)
    date = models.DateTimeField(verbose_name=_("Date"),default=timezone.now)
    def __str__(self):
        return str(self.proudct)