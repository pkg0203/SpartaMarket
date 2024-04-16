from django.shortcuts import render,redirect
import ctypes

# Create your views here.
def show(request):
    if request.user.is_authenticated:
        return render(request,"products/show.html")
    else :
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")