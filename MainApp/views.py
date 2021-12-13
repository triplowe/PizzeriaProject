from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza, Topping, Comment, Image

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
    comments = pizza.comment_set.all()
    if request.method == 'GET':
        image = pizza.image_set.all()
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments, 'image':image}
    return render(request, 'MainApp/pizza.html', context)

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()

            return redirect('MainApp:pizza', pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'MainApp/comment.html', context)


