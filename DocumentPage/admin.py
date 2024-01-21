from django.contrib import admin
from .models import Document, DocumentType, Company, Attachment


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('number', 'published_date', 'company', 'document_type', 'amount', 'vat', 'subject', 'signed_by')
    search_fields = ('number', 'company__name', 'document_type__name', 'subject', 'signed_by')
    list_filter = ('published_date', 'company', 'document_type')

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'address')
    search_fields = ('name', 'tax_id')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file',)
