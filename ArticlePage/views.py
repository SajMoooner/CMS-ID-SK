from django.shortcuts import render

# Create your views here.

def articlePage(request):
    return render(request, 'ArticlePage/article.html')
