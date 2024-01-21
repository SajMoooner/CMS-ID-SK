from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document-list'),
    path('api/get_documents/', views.get_documents, name='get_documents'),
    path('api/get_document_types/', views.get_document_types, name='get_document_types'),
    path('api/get_companies/', views.get_companies, name='get_companies'),
    path('api/get_attachments/', views.get_attachments, name='get_attachments'),
  
]
