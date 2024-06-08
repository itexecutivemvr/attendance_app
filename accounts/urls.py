from django.urls import path
from . import views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('attend',views.attend,name='attend'),
    path('dashboard/',views.dashboard, name='dashboard'),
]