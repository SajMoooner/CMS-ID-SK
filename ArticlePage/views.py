from django.shortcuts import render, get_object_or_404
from MainPage.models import Category, Subcategory
from .models import Article


# Create your views here.

def articlePage(request, article_id):
    categories = Category.objects.all()
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'categories': categories,
        'article': article,
    }
    return render(request, 'ArticlePage/article.html', context)

