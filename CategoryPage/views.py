from django.shortcuts import render
from MainPage.models import Category, Subcategory
from ArticlePage.models import Department, TargetAudience, Article, Subtitle, LifeSituation
from django.http import JsonResponse

def categoryPage(request, kat, zivotna, komu, oddelenie, text):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'CategoryPage/category.html', context)


def get_articles(request):
    articles = list(Article.objects.values())  # Získanie článkov a konverzia na zoznam slovníkov
    return JsonResponse({'articles': articles})

def get_target_audiences(request):
    target_audiences = list(TargetAudience.objects.values())  # Získanie cieľových skupín a konverzia na zoznam slovníkov
    return JsonResponse({'target_audiences': target_audiences})

def get_departments(request):
    departments = list(Department.objects.values())  # Získanie oddelení a konverzia na zoznam slovníkov
    return JsonResponse({'departments': departments})

def get_category(request):
    categories = list(Category.objects.values())  # Získanie kategórií a konverzia na zoznam slovníkov
    return JsonResponse({'categories': categories})

def get_life_situations(request):
    life_situations = list(LifeSituation.objects.values())  # Získanie životných situácií a konverzia na zoznam slovníkov
    return JsonResponse({'life_situations': life_situations})