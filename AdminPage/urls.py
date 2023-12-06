from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeAdmin, name='homeAdmin'),
    path('kategoriaAdmin/', views.categoryAdmin, name='categoryAdmin'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('category/update/<int:category_id>/', views.update_category, name='update_category'),
    path('pridanieClanku/', views.articleAdmin, name='articleAdmin'),
    path('upravaClanku', views.updateArticle, name='articleAdmin'),
    path('odstranenieClanku', views.deleteArticle, name='deleteArticle'),
    path('vsetkyClanky', views.allArticles, name='articleAdmin'),
]