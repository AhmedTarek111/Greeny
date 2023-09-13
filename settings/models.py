from django.db import models

class Company_information(models.Model):
    
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    company_email=models.EmailField()
    phone=models.IntegerField()
    description = models.TextField()
    logo=models.ImageField()
    facebook_link=models.EmailField()
    twiter_link=models.EmailField()
    linkedin_link=models.EmailField()
    instagram_link=models.EmailField()
    pintrest_link=models.EmailField()
    android_app= models.URLField()
