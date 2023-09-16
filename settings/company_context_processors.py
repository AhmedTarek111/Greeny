from .models import Company_information

def company_data(request):
    data = Company_information.objects.last()
    
    return {'company_data':data}