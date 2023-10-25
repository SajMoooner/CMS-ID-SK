from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeAdmin, name='homeAdmin'),
]