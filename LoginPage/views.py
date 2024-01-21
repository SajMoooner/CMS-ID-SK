from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/uvod/')
        else:
            return render(request, 'LoginPage/login.html', {'error_message': 'Zadali ste nesprávne meno alebo heslo.'})
    return render(request, 'LoginPage/login.html')

