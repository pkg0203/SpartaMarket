from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductsForm
import ctypes

# Create your views here.
def show(request):
    if request.user.is_authenticated:
        products = Products.objects.all()
        context={
            "products" : products
        }
        return render(request,"products/show.html",context)
    else :
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")
    
def create(request):
    if request.method=="GET":
        form = ProductsForm()
        context = {
            "form" : form,
        }
        return render(request,"products/create.html",context)
    elif request.method=="POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            product=form.save(commit=False)
            product.author=request.user
            product.save()
        return redirect("products:show")