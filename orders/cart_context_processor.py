from .models import Cart,CartDetail
from django.contrib.auth.models import User

def get_create_cart(request):
    if request.user.is_authenticated:
        cart,created =Cart.objects.get_or_create(user=request.user , status='In Progress')
        if  not created :
            cart_detail=CartDetail.objects.filter(cart=cart)
            return {'cart_detail':cart_detail,'cart_data':cart}
        return {'cart_data':cart}
    else:
        return {} 
