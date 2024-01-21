from MainPage.models import Category, Subcategory
from django.contrib.auth.decorators import login_required
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
from .forms import ArticleForm, SubtitleForm, ArticleFilterForm, CategorySelectForm,DocumentForm
from ArticlePage.models import Article, Subtitle, Category, TargetAudience, Department, LifeSituation
from django.http import JsonResponse
from DocumentPage.models import Document, Attachment, Company, DocumentType



@login_required
def homeAdmin(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    context = {
        'is_uradnik': 'Úradnik' in user_groups,
        'is_fakturant': 'Fakturant' in user_groups,
        'is_spravca': 'Správca' in user_groups,
        'is_superadmin': 'SuperAdmin' in user_groups,
    }
    return render(request, 'AdminPage/homeAdmin.html', context)

@login_required
def categoryAdmin(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'AdminPage/categoryAdmin.html', context)

#--------Pridanie clanku----------------#
@login_required
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
@login_required
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

@login_required
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
@login_required
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
@login_required
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
@login_required
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

#--------Menu----------------#

@login_required
def addMenu(request):
    selected_category_id = None
    category_form = CategorySelectForm(request.POST or None)

    if request.method == 'POST':
        if 'new_name' in request.POST:  # Přidání nové podkategorie
            new_name = request.POST.get('new_name', '')
            new_link = request.POST.get('new_link', '')
            selected_category_id = request.POST.get('category_id', '')

            if new_name and selected_category_id:
                selected_category = Category.objects.get(id=selected_category_id)
                Subcategory.objects.create(category=selected_category, name=new_name, link=new_link)
                

        elif category_form.is_valid():
            selected_category = category_form.cleaned_data['category']
            selected_category_id = str(selected_category.id) if selected_category else None

        # Uložení vybrané kategorie do session
        request.session['selected_category_id'] = selected_category_id

    else:  # GET request
        # Obnovení vybrané kategorie ze session
        selected_category_id = request.session.get('selected_category_id')

    if selected_category_id:
        # Vytvoření formuláře s výchozí hodnotou
        category_form = CategorySelectForm(initial={'category': selected_category_id})
        subcategories = Subcategory.objects.filter(category_id=selected_category_id)
    else:
        subcategories = []

    return render(request, 'AdminPage/addMenu.html', {
        'category_form': category_form,
        'subcategories': subcategories,
    })


@login_required
def delete_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    subcategory.delete()
    return redirect('/uvod/menu')  # Redirekt zpět na seznam podkategorií

@login_required
def edit_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)

    if request.method == 'POST':
        subcategory.name = request.POST.get('name', '')
        subcategory.link = request.POST.get('link', '')
        subcategory.save()
        return redirect('/uvod/menu')  # nebo jiná URL pro návrat

    # Pokud je GET požadavek, zobrazte stránku pro úpravu (nebo můžete přesměrovat jinam)
    return render(request, '/uvod/menu', {'subcategory': subcategory})

#--------Pridanie dokumentu----------------#

@login_required
def addDocument(request):
    if request.method == 'POST':
        doc_form = DocumentForm(request.POST, request.FILES)

        if doc_form.is_valid():
            document = doc_form.save(commit=False)
            document.save()
            # Priradenie príloh k dokumentu
            for file in request.FILES.getlist('attachments'):
                Attachment.objects.create(file=file, document=document)
            
            doc_form.save_m2m()  # Uloženie ManyToMany vzťahov
            return redirect('/uvod')  # Presmerovanie po úspešnom uložení

    else:
        doc_form = DocumentForm()

    return render(request, 'AdminPage/addDocument.html', {'form': doc_form})


@login_required
def viewDocuments(request):
    documents = Document.objects.all()
    return render(request, 'AdminPage/deleteDocument.html', {'documents': documents})

@login_required
def deleteDocument(request, document_id):
    if request.method == 'POST':
        Document.objects.filter(id=document_id).delete()
        return redirect('viewDocuments')
    

@login_required
def updateDocument(request):
    document_types = DocumentType.objects.all()
    selected_document = request.GET.get('document')

    if request.method == 'POST':
        document_id = request.POST.get('document_id')
        if document_id:
            document = get_object_or_404(Document, id=document_id)
            form = DocumentForm(request.POST, request.FILES, instance=document)
            if form.is_valid():
                form.save()
                return redirect('updateDocument')
        else:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('updateDocument')
    else:
        form = DocumentForm()
        if selected_document:
            selected_document = int(selected_document)
            document = get_object_or_404(Document, id=selected_document)
            form = DocumentForm(instance=document)

    return render(request, 'AdminPage/updateDocument.html', {
        'form': form,
        'document_types': document_types,
        'selected_document': selected_document
    })