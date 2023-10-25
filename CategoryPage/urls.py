from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoryPage, name='categoryPage'),
]