from django.shortcuts import render
from MainPage.models import Category, Subcategory 
from .models import Document, DocumentType, Company, Attachment
from django.http import JsonResponse

def document_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'DocumentPage/documents.html', context)

def get_documents(request):
    document_type_id = request.GET.get('document_type_id')
    if document_type_id:
        documents = Document.objects.filter(document_type_id=document_type_id)
    else:
        documents = Document.objects.all()

    documents_data = []
    for document in documents:
        attachments = document.attachments.all()
        attachments_list = [att.file.url for att in attachments]

        documents_data.append({
            "id": document.id,
            "number": document.number,
            "published_date": document.published_date,
            "company_id": document.company.id,
            "document_type_id": document.document_type.id,
            "amount": str(document.amount),
            "vat": str(document.vat),
            "subject": document.subject,
            "signed_by": document.signed_by,
            "attachments": attachments_list
        })

    return JsonResponse(documents_data, safe=False)

def get_document_types(request):
    document_types = list(DocumentType.objects.values())
    return JsonResponse(document_types, safe=False)

def get_companies(request):
    companies = list(Company.objects.values())
    return JsonResponse(companies, safe=False)

def get_attachments(request):
    attachments = list(Attachment.objects.values())
    return JsonResponse(attachments, safe=False)