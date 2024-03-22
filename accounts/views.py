from django.views.generic import DetailView
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Profile, ContactNumber,DeliveryAddress,Delivery_Address_CHOICES,CONTACT_NUMBER_CHOICES
from .models import ContactNumber, DeliveryAddress
from .forms import UserSignupForm,ActivationCodeForm
from django.contrib.auth.models import User

def profileview(request):
    if not request.user.is_anonymous:
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
    else: 
        return redirect('/accounts/login/')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()
            user = User.objects.get(username =username)
            user.is_active = False
            profile= Profile.objects.get(user=user)
            send_mail(
                "Activate your account",
                f'''Welcome Mr/s {username} to Greeny.
                    use this code {profile.code}
                ''',
                f"ahmed@gmail.com",
                [f"{email}"],
                fail_silently=False,
            )
            return redirect(f'/accounts/activate/{username}')
    else:
        form = UserSignupForm()
    
    return render(request,'registration/register.html',{'form':form})
    
def activate(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user.id)
    if request.method == 'POST':
        form = ActivationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.user.is_active = True
                profile.user.is_staff = True #can access to the admin panel 
                profile.code = ''
                profile.save()
                return redirect ('/')
        
    else:
        form = ActivationCodeForm()
    return render(request,'registration/code.html',{'form':form})