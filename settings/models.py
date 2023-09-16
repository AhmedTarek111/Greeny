from django.db import models

class Company_information(models.Model):
    
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    company_email=models.EmailField()
    phone=models.CharField(max_length=20)
    description = models.TextField()
    logo=models.ImageField()
    facebook_link=models.URLField()
    twiter_link=models.URLField()
    linkedin_link=models.URLField()
    instagram_link=models.URLField()
    pintrest_link=models.URLField()
    android_app= models.URLField()
    
    def __str__(self):
        return self.name