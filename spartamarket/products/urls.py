from django.urls import path
from . import views

app_name = "products"
urlpatterns=[
    path('show/',views.show,name='show'),
    path('create/',views.create,name='create'),
]