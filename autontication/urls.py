
from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login),
    path('registration/', views.auth_registration),
    path('forget/', views.forget_password),
    path('logout/', views.auth_logout),
]
