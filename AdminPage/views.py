from MainPage.models import Category, Subcategory
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages  # Ak chcete zobrazovať upozornenia
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm, SubtitleForm, ArticleFilterForm
from ArticlePage.models import Article, Subtitle, Category, TargetAudience, Department
from django.http import JsonResponse


# Create your views here.

def homeAdmin(request):
    return render(request, 'AdminPage/homeAdmin.html')

def categoryAdmin(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'AdminPage/categoryAdmin.html', context)

#--------Pridanie clanku----------------#

def articleAdmin(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        subtitle_forms = [SubtitleForm(request.POST, request.FILES, prefix=str(x)) for x in range(5)]

        if article_form.is_valid():
            article = article_form.save()

            for sf in subtitle_forms:
                if sf.is_valid() and sf.cleaned_data.get('text'):  # Zde se kontroluje, zda je text podtitulku vyplněný
                    subtitle = sf.save(commit=False)
                    subtitle.article = article
                    subtitle.save()

            return redirect('homeAdmin')
    else:
        article_form = ArticleForm()
        subtitle_forms = [SubtitleForm(prefix=str(x)) for x in range(5)]

    return render(request, 'AdminPage/addArticle.html', {'article_form': article_form, 'subtitle_forms': subtitle_forms})



#--------Pridanie kategorie----------------#

@require_POST
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('categoryAdmin'))

def categoryAdmin(request):
    if request.method == 'POST':
        new_category_name = request.POST.get('new_category_name').strip()  # Získajte nový názov kategórie a odstráňte biele znaky

        if new_category_name:  # Skontrolujte, či je názov kategórie neprázdny
            # Skontrolujte, či už kategória s takým názvom neexistuje
            if not Category.objects.filter(name=new_category_name).exists():
                Category.objects.create(name=new_category_name)  # Vytvorte novú kategóriu
                messages.success(request, 'Nová kategória bola pridaná.')  # Voliteľné: zobrazte správu o úspechu
            else:
                messages.error(request, 'Kategória s týmto názvom už existuje.')  # Voliteľné: zobrazte správu o chybe
            return redirect('/uvod')  # Presmerujte späť na stránku s kategóriami

    # Ak metóda nie je POST, iba zobrazíme stránku
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'AdminPage/categoryAdmin.html', context)

@require_POST
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    new_name = request.POST.get('new_name', '')

    if new_name:
        category.name = new_name
        category.save()
        messages.success(request, 'Kategória bola úspešne upravená.')  # Optional: add a success message
    else:
        messages.error(request, 'Názov kategórie nemôže byť prázdny.')  # Optional: add an error message

    return redirect('categoryAdmin')

#---------Uprava clanku-----------------#
def updateArticle(request):
    form = ArticleFilterForm(request.POST or None)
    selected_article = None
    subtitles = []
    selected_category_id = None 
    selected_article_id = None  

    if request.method == 'POST':
        category_id = request.POST.get('category')
        article_id = request.POST.get('article')
        
        if 'load_articles' in request.POST and category_id:
            selected_category_id = category_id
            form.fields['article'].queryset = Article.objects.filter(category_id=category_id)

        elif 'select_article' in request.POST and article_id:
            selected_article_id = article_id
            selected_article = get_object_or_404(Article, id=article_id)
            subtitles = selected_article.subtitles.all()
            if category_id:
                selected_category_id = category_id
                form.fields['article'].queryset = Article.objects.filter(category_id=category_id)

        elif 'update_article' in request.POST:
            article_id = request.POST.get('article_id')
            if article_id:
                selected_article = get_object_or_404(Article, id=article_id)
                selected_article.title = request.POST.get('title', selected_article.title)
                selected_article.content = request.POST.get('content', selected_article.content)
                
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    selected_article.image.save(image.name, image, save=True)
                selected_article.save()
                
                # Aktualizace titulků podčlánků
                for subtitle in selected_article.subtitles.all():
                    subtitle.title = request.POST.get(f'subtitle_title_{subtitle.id}', subtitle.title)
                    subtitle.text = request.POST.get(f'subtitle_text_{subtitle.id}', subtitle.text)
                    if f'subtitle_image_{subtitle.id}' in request.FILES:
                        image = request.FILES[f'subtitle_image_{subtitle.id}']
                        subtitle.image.save(image.name, image, save=True)
                    subtitle.save()
                
                # Přesměrování po úspěšné aktualizaci
                return redirect('/uvod')
            
    return render(request, 'AdminPage/updateArticle.html', {
                'form': form,
                'selected_article': selected_article,
                'subtitles': subtitles,
                'selected_category_id': selected_category_id,
                'selected_article_id': selected_article_id
  })
    
#--------Odstranenie clanku----------------#
    
def deleteArticle(request):
    # Filtrování článků
    articles_query = Article.objects.all()
    category_id = request.GET.get('category')
    target_audience_id = request.GET.get('target_audience')
    department_id = request.GET.get('department')

    if category_id:
        articles_query = articles_query.filter(category_id=category_id)
    if target_audience_id:
        articles_query = articles_query.filter(target_audience_id=target_audience_id)
    if department_id:
        articles_query = articles_query.filter(department_id=department_id)

    # Odstranění článku
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Article, id=article_id)
            article.delete()
            return redirect('deleteArticle')  # Zde předpokládám, že 'deleteArticle' je název URL pro tento pohled

    categories = Category.objects.all()
    target_audiences = TargetAudience.objects.all()
    departments = Department.objects.all()

    context = {
        'articles': articles_query,
        'categories': categories,
        'target_audiences': target_audiences,
        'departments': departments,
    }
    return render(request, 'AdminPage/deleteArticle.html', context)

#--------Vsetky clanky----------------#

def allArticles(request):
    articles = Article.objects.all()

    # Filtrování podle kategorie, cílového publika a oddělení
    category_id = request.GET.get('category')
    target_audience_id = request.GET.get('target_audience')
    department_id = request.GET.get('department')

    if category_id:
        articles = articles.filter(category_id=category_id)
    if target_audience_id:
        articles = articles.filter(target_audience_id=target_audience_id)
    if department_id:
        articles = articles.filter(department_id=department_id)

    categories = Category.objects.all()
    target_audiences = TargetAudience.objects.all()
    departments = Department.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
        'target_audiences': target_audiences,
        'departments': departments,
    }
    return render(request, 'AdminPage/allArticles.html', context)






    
