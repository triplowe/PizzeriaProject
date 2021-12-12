from django.shortcuts import render

# Create your views here.
def index(request):
    """Home Page for Pizzeria"""
    return render(request, 'MainApp/index.html')