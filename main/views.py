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


def edit_coffee(request, coffee_id):
    context = {}
    coff = Coffee.objects.get(id=coffee_id)
    context['coffee'] = coff
    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coff)
        context['form'] = form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m() # specific to many to many
            return redirect("home")
        else:
            return render(request, 'edit_coffee.html', context)
    else:
        form = CoffeeForm(instance=coff)
        context['form'] = form
        return render(request, 'edit_coffee.html', context)


def delete_coffee(request, coffee_id):
    Coffee.objects.get(id=coffee_id).delete()
    return redirect("home")

def create_bean(request):
    context = {}
    if request.method == "POST":
        form = BeanForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'create_bean.html', context)
    else:
        form = BeanForm()
        context['form'] = form
        return render(request, 'create_bean.html', context)


def edit_bean(request, bean_id):
    context = {}
    bean = Bean.objects.get(id=bean_id)
    context['bean']=bean
    if request.method == "POST":
        form = BeanForm(request.POST, instance=bean)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'edit_bean.html', context)
    else:
        form = BeanForm(instance=bean)
        context['form'] = form
        return render(request, 'edit_bean.html', context)

def delete_bean(request, bean_id):
    Bean.objects.get(id=bean_id).delete()
    return redirect("home")
