from django.shortcuts import render, redirect
from .models import *
from .forms import PastryForm, IngredientsForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            user= authenticate(request, username =username, password=password)
        if user is not None:
            login(request,user)
            return redirect("create-page")
        else:
            return messages.error(request,"Username or Password is incorrect")
    return render(request, "product/login.html")

def logoutPage(request):
    logout(request)
    return redirect('login-page')
def index(request):
    pasteles = Pastry.objects.all()
    context = {"pasteles": pasteles}
    return render(request, "product/home.html", context)


@login_required(login_url="login-page")
def product(request, pk):
    pasteles = Pastry.objects.get(id=pk)
    context = {"pasteles": pasteles, "pk": pk}
    return render(request, "product/food.html", context)



@login_required(login_url="login-page")
def createproduct(request):
    form = PastryForm()
    pasteles = Pastry.objects.all()
    if request.method == "POST":
        form = PastryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form,"pasteles":pasteles}
    return render(request, "product/newproduct.html", context)

@login_required(login_url="login-page")
def updateproduct(request, pk):
    products = Pastry.objects.get(id=pk)

    form = PastryForm(instance=products)

    if request.method == "POST":
        form = PastryForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form, "product": products}
    return render(request, "product/newproduct.html/", context)


@login_required(login_url="login-page")
def createingredient(request):
    form = IngredientsForm(request.POST)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "product/newingredient.html", context)


@login_required(login_url="login-page")
def deleteproduct(request, pk):
    product = Pastry.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect("home-page")
    context = {"product": product}
    return render(request, "product/deleteproduct.html", context)
