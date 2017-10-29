from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..travellogin.models import User, Travel
from django.shortcuts import render, redirect
from django.contrib import messages

def success(request):
    # print ("************** success page ********************")
    # try:
    #     request.session['user_id']
    # except KeyError:
    #     return redirect('/')
    # userq = User.objects.get(id=request.session['user_id'])
    #
    # context = {
    #     'user': User.objects.get(id=request.session['user_id'])
    #     # 'userq': Travel.objects.filter(name = userq)
    # }
    user_name = User.objects.get(id=request.session['User_id'])
    print ("*****username*******", user_name.name)

    context = {
        # 'User': User.objects.get(id=request.session['User_id'])
        'users'  : Travel.objects.filter(user=User.objects.get(id=request.session['User_id'])),
        'others' : Travel.objects.exclude(user=User.objects.get(id=request.session['User_id'])),
        'homeuser' :  User.objects.get(id=request.session['User_id'])
        }
    return render(request, 'traveldash/success.html', context)

def logout(request):
    try:
        #print('**** return render ****')
        del request.session['User_id']
        request.session.modified = True
        return redirect('/')

    except KeyError:
        #print('**** redirect ****')
        return redirect('/')

# def additems(request):
#     try:
#         request.session['user_id']
#     except KeyError:
#         return redirect('/')
#     context = {
#         'user': User.objects.get(id=request.session['user_id'])
#     }
#     return render(request, 'withlist_items/withlist_items.html', context)
# # Create your views here.

def showitems(request):
    return redirect('plan:showitems')
