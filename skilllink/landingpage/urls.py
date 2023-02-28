from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('cources/', views.cources),
    path('contact', views.contact),
    path('register', views.register),
]