from django.shortcuts import render,redirect
from .forms import ProductsForm
import ctypes

# Create your views here.
def show(request):
    if request.user.is_authenticated:
        return render(request,"products/show.html")
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