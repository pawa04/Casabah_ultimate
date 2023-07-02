from django.shortcuts import render, redirect
from .models import *
from .forms import PastryForm, IngredientsForm


# Create your views here.

def index(request):
    pasteles = Pastry.objects.all()
    context = {"pasteles": pasteles}
    return render(request, "product/home.html", context)


def product(request, pk):
    pasteles = Pastry.objects.all()
    context = {"pasteles": pasteles, "pk": pk}
    return render(request, "product/food.html", context)


def createproduct(request):
    form = PastryForm()

    if request.method == "POST":
        form = PastryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "product/newproduct.html", context)


def updateproduct(request, pk):
    products = Pastry.objects.get(id=pk)
    print(products)
    form = PastryForm(instance=products)

    if request.method == "POST":
        form = PastryForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect("")
    context = {"form": form, "product":products}
    return render(request, "product/newproduct.html/", context)


def createingredient(request):
    form = IngredientsForm(request.POST)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "product/newingredient.html", context)
