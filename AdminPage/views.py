from django.shortcuts import render

# Create your views here.

def homeAdmin(request):
    return render(request, 'AdminPage/homeAdmin.html')
