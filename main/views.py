from django.shortcuts import render, redirect
from .forms import *

def home(request):
    return render(request, 'home.html', {})

def create_coffee(request):
    context = {}
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        context['form'] = form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m() # specific to many to many
            return redirect("home")
        else:
            return render(request, 'create_coffee.html', context)
    else:
        form = CoffeeForm()
        context['form'] = form
        return render(request, 'create_coffee.html', context)
