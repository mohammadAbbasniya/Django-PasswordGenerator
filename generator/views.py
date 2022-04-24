from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        alphabets.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        alphabets.extend(list('012345678'))

    if request.GET.get('special'):
        alphabets.extend(list('!@#$%^&*(){}_-+=.'))

    n = 80
    try:
        if request.GET.get('length'):
            n = int(request.GET.get('length'))
    except:
        n = 80

    the_pass = ''
    for i in range(n):
        the_pass += random.choice(alphabets)

    return render(request, 'generator/password.html', {
        'password': the_pass
    })
