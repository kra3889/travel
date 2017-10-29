from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strptime, strftime

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# apps.secret_key = "keepitasecretbozo"

def index(request):
    print ("***** view.py file index function ****")

    return render(request, "travellogin/index.html")

def register(request):
    print ('*************** error function ************')
    result = User.objects.user_validator(request.POST)
    if type(result) == list:
        for err in result:
                messages.error(request, err)
        return redirect('/')
    request.session['User_id'] = result.id
    messages.success(request, "Successfully registered!")
    context = {
        'User': User.objects.get(id=request.session['User_id'])
    }
    return render(request, 'traveldash/success.html', context)



    # return redirect('/'+id)

def login(request):
    print ("*********** login page   ***********")
    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for item in result:
            messages.error(request, item)
        return redirect('/')
    request.session['User_id'] = result.id
    mylogin = User.objects.get(id=request.session['User_id'])

    messages.success(request, "Welcom Back, Successfully logged in!")
    context = {
        'User': User.objects.get(id=request.session['User_id']),
        'uname' : mylogin.name
    }
    # return render(request, 'traveldash/success.html', context)
    return redirect ('login:success')

def success(request):
    mylogin = User.objects.get(id=request.session['User_id'])
    print ("*************** made it to dashboard")
    try:
        request.session['User_id']
    except KeyError:
        return redirect('dashboard:success')

    print ("*****************************************************")
    # print (userq)
    print ("******************************************************")


    return redirect ('dashboard:success')
# Create your views here.
