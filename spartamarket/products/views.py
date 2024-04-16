from django.shortcuts import render
from . import views

# Create your views here.
def show(request):
    return render(request,"products/show.html")