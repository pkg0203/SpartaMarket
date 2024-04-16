from django.urls import path
from . import views

app_name = "products"
urlpatterns=[
    path('show/',views.show,name='show'),
    path('create/',views.create,name='create'),
    path('<int:pk>/detail',views.detail,name='detail'),
    path('<int:pk>/update',views.update,name='update'),
    path('<int:pk>/delete',views.delete,name='delete'),
]