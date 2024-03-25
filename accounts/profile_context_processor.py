from .models import Profile
from django.shortcuts import render

def profile_details(request):
    profile = Profile.objects.get(user= request.user)
    context ={
        
        'profile':profile,
        
        }
    return  context