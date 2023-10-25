from django.urls import path
from . import views

urlpatterns = [
    path('', views.articlePage, name='articlePage'),
]