from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_codes import generate_code
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to='profile')
    code = models.CharField(max_length=100,default=generate_code)
    
    @receiver(post_save,sender=User)    
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(
                user = instance
            )
CONTACT_NUMBER_CHOICES = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
    
)
class ContactNumber(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_contact_number')
    number = models.CharField(max_length=20)
    type= models.CharField(max_length=50,choices=CONTACT_NUMBER_CHOICES)
    
    
Delivery_Address_CHOICES = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Other','Other'),
    
)
class DeliveryAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_delivery_address') 
    type = models.CharField(max_length=80 , choices=Delivery_Address_CHOICES)
    address = models.CharField(max_length=200 )
    notes = models.TextField(null=True,blank=True)
    

    