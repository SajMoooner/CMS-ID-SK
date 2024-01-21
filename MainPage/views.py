from django.shortcuts import render
from .models import Category, Subcategory 
from ArticlePage.models import Article,LifeSituation,Department,TargetAudience
from django.http import JsonResponse
from DocumentPage.models import Document

# Create your views here.

def home(request):
    categories = Category.objects.all()
    # Získajte všetky články a zoradiť ich od najnovšieho okrem kategórie "Návody"
    articles =  Article.objects.exclude(category__name='Návody').order_by('-created_at')
    life_situations = LifeSituation.objects.all()
    target_audiences = TargetAudience.objects.all() 
    departments = Department.objects.all() 

    hero_article = articles.first()
    other_articles = articles[1:4]
    
    # Clanky v kde kategoria je "Návody" a target audience je "Občan"
    navody_articles = Article.objects.filter(category__name='Návody', target_audience__name='Občan').order_by('-created_at')[:5]
    
    # Clanky v kde kategoria je "Návody" a target audience je "Podnikateľ"
    navody_articles_podnikatel = Article.objects.filter(category__name='Návody', target_audience__name='Podnikateľ').order_by('-created_at')[:5]
    
    # Načítanie posledných 10 dokumentov
    latest_documents = Document.objects.all().order_by('-published_date')[:10]

    # Rozdelenie dokumentov do dvoch stĺpcov
    documents_column_one = latest_documents[:5]
    documents_column_two = latest_documents[5:10]

    context = {
        'categories': categories,
        'hero_article': hero_article,
        'other_articles': other_articles,
        'articles': articles,
        'life_situations': life_situations,
        'target_audiences': target_audiences,  
        'departments': departments,  
        'navody_articles': navody_articles,
        'navody_articles_podnikatel': navody_articles_podnikatel,
        'documents_column_one': documents_column_one,
        'documents_column_two': documents_column_two,
    }
    return render(request, 'MainPage/main.html', context)

