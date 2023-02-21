from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='skilllink-home'),
    path('about/', views.about, name='skilllink-about')
]