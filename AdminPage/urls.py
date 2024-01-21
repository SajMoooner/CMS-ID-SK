from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.homeAdmin, name='homeAdmin'),
    path('kategoriaAdmin/', views.categoryAdmin, name='categoryAdmin'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('category/update/<int:category_id>/', views.update_category, name='update_category'),
    path('pridanieClanku/', views.articleAdmin, name='articleAdmin'),
    path('upravaClanku', views.updateArticle, name='articleAdmin'),
    path('odstranenieClanku', views.deleteArticle, name='deleteArticle'),
    path('vsetkyClanky', views.allArticles, name='articleAdmin'),
    path('odhlasenie/', LogoutView.as_view(next_page='login'), name='logout'),
    path('menu/', views.addMenu, name='addMenu'),
    path('odstranit-podkategorii/<int:subcategory_id>/', views.delete_subcategory, name='odstranit_podkategorii'),
    path('upravit-podkategorii/<int:subcategory_id>/', views.edit_subcategory, name='upravit_podkategorii'),
    path('pridanieDokumentu/', views.addDocument, name='addDocument'),
    path('odstranenieDokumentu/', views.viewDocuments, name='viewDocuments'),
    path('odstranenieDokumentu/delete/<int:document_id>/', views.deleteDocument, name='deleteDocument'),
    path('upravaDokumentu/', views.updateDocument, name='updateDocument'),
    ]