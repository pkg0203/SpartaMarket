from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/mypage/', views.mypage, name='mypage'),
    path('<int:pk>/follow/', views.follow, name='follow'),
    path('<int:pk>/update_profile/', views.update_profile, name='update_profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
