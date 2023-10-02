from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class CartAPI(GenericAPIView):
    def get(self,request,*args, **kwargs):
        cart,created =Cart.objects.get_or_create(user=User.objects.get(username=self.kwargs['username']), status='In Progress')
        data= CartSerializers(cart).data
        return Response(data)
        