from django.urls import path,re_path
from . import views

urlpatterns = [
     re_path(r'kat=(?P<kat>[\w-]+)/zivotna=(?P<zivotna>[\w-]+)/komu=(?P<komu>[\w-]+)/oddelenie=(?P<oddelenie>[\w-]+)/text=(?P<text>[^/]+)/$', views.categoryPage, name='category_detail'),
     path('api/get-articles/', views.get_articles, name='get_articles'),
     path('api/get-target-audiences/', views.get_target_audiences, name='get_target_audiences'),
     path('api/get-departments/', views.get_departments, name='get_departments'),
     path('api/get-category', views.get_category, name='get_category'),
     path('api/get-life-situations/', views.get_life_situations, name='get_life_situations')
]
