from django.urls import path
from . import views

urlpatterns = [
    path("home/",view=views.home, name="home"),
    path("login/",view=views.loginPage, name="login"),
    path("signups/",view=views.signups, name="signups"),
    path('logout/',views.LogoutPage,name='logout'),
    path('',views.loginPage,name="login"),
]