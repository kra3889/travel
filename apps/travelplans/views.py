from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..travellogin.models import User, Travel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

print ('*' * 40)
print ("*********** Plan Details *************")
print ('*' * 40)

def index(request):
    context = {
        'User': User.objects.get(id=request.session['User_id'])
    }

    print ("***** view.py from withlist items file index function ****")


    return render(request, "travelplans/plans_trips.html", context)

def planlistadd(request):
    print ("*********** adding item_id page   ***********")
    # print ("**************** in additem    user2)", user2)
    # user2=User.objects.get(id=request.session['User_id'])
    user2=request.session['User_id']
    print("********** user2----->", user2)
    result = Travel.objects.travelplanadd(request.POST, user2)
    if type(result) == list:
        for item in result:
            messages.error(request, item)
        return redirect('/')
    request.session['item_id'] = result.id

    print ("******* in add review   *******", request.session['item_id'])
    messages.success(request, "Successfully Added Item!")
    return redirect('plans:additem')


def additem(request):

    user2=request.session['user_id']
    print (user2)
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])

    }
    print ("***************** regobj ***********",user.objects)
    return render(request, 'travelplans/plans_trips.html', context)
#*****************************************************************

def home(request):
    # User.objects.get(id=request.session['user_id'])
    print ("*********************trying for user id in home function-1")

    print ("***************** regobj ***********",User.objects)
    #return redirect('dashboard:success'

    context = {
        'User': User.objects.get(id=request.session['User_id'])
    }

    return redirect(reverse('dashboard:success'))

def logout(request):
    try:
        #print('**** return render ****')
        request.session['User_id'] = ""
        return render(request, 'travellogin/index.html')
    except KeyError:
        #print('**** redirect ****')
        request.session['User_id'] = ""
        return redirect('/')

def showitems(request, id):

    users2 = User.objects.get(id=request.session['User_id'])

    print (users2.id)

    print('===================== travel item is {} ==================='.format(users2.id))
    travels = Travel.objects.get(id=id)
    context = {
        # 'travel' :   Travel.objects.get(id = id),
         'users2' : User.objects.get(id=request.session['User_id'])

        }
    print ("***************** regobj ***********",User.objects)
    return render(request, 'withlist_items/withlist_showitems.html', context)


def removeitems(request, id):
    print ('************remove items **!!!**********', id)
    rmuser = User.objects.get(id=request.session['User_id'])
    travelplan = Travel.objects.get(id=id)
    travelplan.name.remove(rmuser)
    print ('*************remove complete *************')
    return redirect ('dashboard:success')


def traveladd(request, id):
    print ('************travel adds ************', id)
    adduser = User.objects.get(id=request.session['User_id'])
    Travel.objects.get(id=id).name.add(adduser)
    return redirect('dashboard:success')

def itemshow(request, id):
    print ("****************show users who want item also ***********")
    homeuser=User.objects.get(id=request.session['User_id'])
    travel= Travel.objects.get(id=id)

    print (travel.name.name)
    context = {
        'travel' : travel,
        'homeuser' : homeuser
        }
    return render(request, 'traveplans/plans_showtrip.html', context)
