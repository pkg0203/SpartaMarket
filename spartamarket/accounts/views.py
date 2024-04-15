from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.http import (
    require_POST,
    require_http_methods
)
from .forms import *

# Create your views here.
def login(request):
    return render(request,"accounts/login.html")

@require_http_methods(["GET","POST"])
def signup(request):
    if request.method=="GET":
        form = CustomUserCreationForm()
        context = {
            "form" : form,
        }
        return render(request,"accounts/signup.html",context)
    else :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user=form.save()
            auth_login(request,user)
            return redirect("index")