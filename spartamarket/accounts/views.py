from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import (
    require_POST,
    require_http_methods
)
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from products.models import Products
from .forms import *
import ctypes


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            next_url = request.GET.get('next') or 'index'
            auth_login(request, form.get_user())
            return redirect(next_url)
        ctypes.windll.user32.MessageBoxW(
            0, "아이디나 비밀번호가 유효하지 않습니다!", "Error", 16)
        return redirect('index')


@require_POST
def logout(request):
    auth_logout(request)
    return redirect("index")


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            auth_login(request, user)
            return redirect("index")


def mypage(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    products = Products.objects.filter(author=pk)
    context = {
        "user": user,
        "products": products,
    }
    return render(request, "accounts/mypage.html", context)


@require_POST
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        pass
    else:
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return redirect('accounts:mypage', user.pk)


@require_POST
def update_profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    user.profile_image = request.FILES
    user.save()
    return redirect('accounts:mypage', pk)
