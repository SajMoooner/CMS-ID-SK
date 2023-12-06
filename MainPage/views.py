from django.shortcuts import render
from .models import Category, Subcategory 
from ArticlePage.models import Article

# Create your views here.

def home(request):
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-created_at')  # Získajte všetky články a zoradiť ich od najnovšieho

    hero_article = articles.first()  
    other_articles = articles[1:4]  

    context = {
        'categories': categories,
        'hero_article': hero_article,
        'other_articles': other_articles,
        'articles': articles,  # Ponecháme pro zobrazení všech článků
    }
    return render(request, 'MainPage/main.html', context)
