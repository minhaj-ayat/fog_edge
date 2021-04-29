import hashlib

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserInfo


# Create your views here.
def login_view(request):
    args = {'valid_login': True}
    return render(request, 'login.html', args)


def home_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phash = str(hashlib.md5(password.encode()).hexdigest())
    args = {'valid_login': True, 'username': username}

    if UserInfo.objects.filter(loginid=username).exists() and UserInfo.objects.filter(passwd=phash).exists():
        return render(request, 'home.html', args)
    else:
        args['valid_login'] = False
        return render(request, 'login.html', args)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if UserInfo.objects.filter(loginid=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            else:
                phash = str(hashlib.md5(password.encode()).hexdigest())
                user = UserInfo.objects.create(loginid=username, passwd=phash)
                user.save()
                print('user created')
                return redirect('/')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/register')
    else:
        return render(request, 'register.html')
