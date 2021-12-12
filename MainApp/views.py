from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.
def index(request):
    """Home Page for Pizzeria"""
    return render(request, 'MainApp/index.html')

def pizzas(request):
    """Page displaying all the pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas':pizzas}
    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'MainApp/pizza.html', context)
