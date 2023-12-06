from django.shortcuts import render
from MainPage.models import Category, Subcategory

def categoryPage(request, category_name):
    categories = Category.objects.all()
    context = {
        'category_name': category_name,
        'categories': categories,
    }
    return render(request, 'CategoryPage/category.html', context)
