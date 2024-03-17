from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile, ContactNumber,DeliveryAddress

def profileview(request):
        user = user=request.user.id
        print(user)
        profile = Profile.objects.get(user=user)
        contact_number= ContactNumber.objects.filter(user=user)
        deliveryaddress = DeliveryAddress.objects.filter(user=user)
        context = {
            'profile':profile,
            'contact_numbers':contact_number,
            'deliveryaddress':deliveryaddress
            }
        return render(request,'registration/profile.html',context)
    

