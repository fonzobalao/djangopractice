from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="practice-home"),
    path('about/', views.about, name="practice-about"),
]