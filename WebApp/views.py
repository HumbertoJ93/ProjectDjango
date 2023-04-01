from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    
    return render(request, 'WebApp/index.html')


def tienda(request):
    
    return render(request, 'WebApp/tienda.html')


