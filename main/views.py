from django.shortcuts import render, redirect
from .forms import *
import datetime

def home(request):
    context = {}
    user = request.user
    context['user'] = user
    today = datetime.date.today()
    context['today']=today
    coffee_list = Coffee.objects.filter(user=user)
    context['coffee_list']=coffee_list
    order_list = Order.objects.filter(user=user, date=today)
    context['order_list']=order_list
    return render(request, 'home.html', context)

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

def create_roast(request):
    context = {}
    if request.method == "POST":
        form = RoastForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'create_roast.html', context)
    else:
        form = RoastForm()
        context['form'] = form
        return render(request, 'create_roast.html', context)


def edit_roast(request, roast_id):
    context = {}
    roast = Roast.objects.get(id=roast_id)
    context['roast']=roast
    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'edit_roast.html', context)
    else:
        form = RoastForm(instance=roast)
        context['form'] = form
        return render(request, 'edit_roast.html', context)

def delete_roast(request, roast_id):
    Roast.objects.get(id=roast_id).delete()
    return redirect("home")

def create_powder(request):
    context = {}
    if request.method == "POST":
        form = PowderForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'create_powder.html', context)
    else:
        form = PowderForm()
        context['form'] = form
        return render(request, 'create_powder.html', context)


def edit_powder(request, powder_id):
    context = {}
    powder = Powder.objects.get(id=powder_id)
    context['powder']=powder
    if request.method == "POST":
        form = PowderForm(request.POST, instance=powder)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'edit_powder.html', context)
    else:
        form = PowderForm(instance=powder)
        context['form'] = form
        return render(request, 'edit_powder.html', context)

def delete_powder(request, powder_id):
    Powder.objects.get(id=powder_id).delete()
    return redirect("home")

def create_syrup(request):
    context = {}
    if request.method == "POST":
        form = SyrupForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'create_syrup.html', context)
    else:
        form = SyrupForm()
        context['form'] = form
        return render(request, 'create_syrup.html', context)


def edit_syrup(request, syrup_id):
    context = {}
    syrup = Syrup.objects.get(id=syrup_id)
    context['syrup']=syrup
    if request.method == "POST":
        form = SyrupForm(request.POST, instance=syrup)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'edit_syrup.html', context)
    else:
        form = SyrupForm(instance=syrup)
        context['form'] = form
        return render(request, 'edit_syrup.html', context)

def delete_syrup(request, syrup_id):
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("home")

def create_order(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee'] = coffee
    if request.method == "POST":
        form = OrderForm(request.POST)
        context['form'] = form
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.coffee = coffee
            order.save()
            return redirect("home")
        else:
            return render(request, 'create_order.html', context)
    else:
        form = OrderForm()
        context['form'] = form
        return render(request, 'create_order.html', context)
