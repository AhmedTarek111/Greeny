from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile, ContactNumber,DeliveryAddress,Delivery_Address_CHOICES,CONTACT_NUMBER_CHOICES
from django.shortcuts import redirect
from django.shortcuts import redirect, render
from .models import ContactNumber, DeliveryAddress

def profileview(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    contact_numbers = ContactNumber.objects.filter(user=user)
    delivery_addresses = DeliveryAddress.objects.filter(user=user)
    types_of_contact_number = [CONTACT_NUMBER_CHOICES[x][0] for x in range(len(CONTACT_NUMBER_CHOICES))]
    types_of_delivery_address = [Delivery_Address_CHOICES[x][0] for x in range(len(Delivery_Address_CHOICES))]
    
    if request.method == 'POST':
        if request.POST.get('create') == 'newcontact':
            data = request.POST
            new_contact = ContactNumber.objects.create(
                user=user,
                number=data.get('number'),
                type=data.get('type')
            )
            new_contact.save()
            return redirect('/accounts/profile/')
        
        elif request.POST.get('create') == 'newaddress':
            data = request.POST
            add_address = DeliveryAddress.objects.create(
                user=user,
                type= data.get('type'),
                address= data.get('address'),
            )
            add_address.save()
      
    return render(request, 'registration/profile.html', {
            'profile': profile,
            'contact_numbers': contact_numbers,
            'types_of_contact_number': types_of_contact_number,
            'deliveryaddresses': delivery_addresses,
            'types_of_delivery_address':types_of_delivery_address,
        })
