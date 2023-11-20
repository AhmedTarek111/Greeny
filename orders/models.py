from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils import timezone
from utils.generate_codes import generate_code
CART_CHOICES=(
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    )

class Cart(models.Model):
  
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart_user')
    status = models.CharField(max_length=50,choices=CART_CHOICES)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL,null=True,blank=True,related_name='cart_coupon')
    total_after_coupon = models.CharField(max_length=30,null=True,blank=True)

    def cart_total(self):
        total = 0
        for i in self.cart_detail.all():
            total += i.total 
        return total 
    
    def __str__(self):
       return str(self.user)

class CartDetail(models.Model):
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_detail')
    products = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True, related_name='cart_detail_products')
    price =  models.FloatField()
    quantity= models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)
    def __str__(self):
        return str(self.cart)

ORDER_STATUS=(
        ('Order Recieved','Order Recieved'),
        ('Order Processed','Order Processed'),
        ('Order Shipped','Order Shipped'),
        ('Order Delivered','Order Delivered'),
        )

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_user')
    code = models.CharField(max_length=15,default=generate_code())
    status = models.CharField(max_length=50,choices=ORDER_STATUS)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL,null=True,blank=True,related_name='order_coupon')
    total_after_coupon = models.CharField(max_length=30,null=True,blank=True)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time= models.DateTimeField(null=True,blank=True)
    
    def __str__(self):    
       return self.code
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_detail')
    products= models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_detail_products')
    price =  models.FloatField()
    quantity= models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)
    
    def __str__(self):
       return str(self.order)

class Coupon(models.Model):
    code=models.CharField(max_length=15 )
    discount =models.IntegerField()
    quantity= models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date =models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
       return self.code

    def save(self, *args, **kwargs):
       week= timezone.timedelta(days=7)
       self.end_date = self.start_date + week
       super(Coupon, self).save(*args, **kwargs)

class Deleviry_fee(models.Model):
    fee = models.FloatField()
    
    def __str__(self):
        return str(self.fee)