from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_name>/', views.categoryPage, name='category_detail'),
]
