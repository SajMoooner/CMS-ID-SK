from django.shortcuts import render

# Create your views here.

def categoryPage(request):
    return render(request, 'CategoryPage/category.html')