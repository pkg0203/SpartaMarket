from django.urls import path
from . import views

app_name = "products"
urlpatterns=[
    path('show/',views.show,name='show'),
    #Products CRUD
    path('create/',views.create,name='create'),
    path('<int:pk>/detail',views.detail,name='detail'),
    path('<int:pk>/update',views.update,name='update'),
    path('<int:pk>/delete',views.delete,name='delete'),
    
    path('<int:pk>/comment',views.create_comment,name='create_comment'),
    path('<int:pk>/comment_delete',views.delete_comment,name='delete_comment'),
    path('<int:pk>/comment_update',views.update_comment,name='update_comment'),
]