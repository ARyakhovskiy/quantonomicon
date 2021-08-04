from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cryptotracker-home'),
    path('about/', views.about, name='cryptotracker-about'),

]

