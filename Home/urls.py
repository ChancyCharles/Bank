from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Login/", views.Login, name='Login'),
    path("Register/", views.Register, name='Register'),
    path("Form/", views.Form, name='Form'),
    path("Button/", views.Button, name='Button'),
    path("logout/", views.logout, name='logout'),
    path("submit/",views.submit,name='submit'),
    path("contact/",views.contact,name='contact')
    ]