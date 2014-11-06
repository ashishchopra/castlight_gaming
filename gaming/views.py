from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from gaming.models import User_Images
from django.contrib.auth.models import User
# Import the model classes we just wrote.

import random

def index(request):
    print request.user.id
    user_images = User_Images.objects.all()
    context = {'user_images': user_images}
    return render(request, 'gaming/index.html', context)

def show_random_user_profile(request):
  users_count = User.objects.count()
  n = random.randint(1,users_count)
  user = User.objects.filter(id=n)[0]	
  if user:
    user_images = User_Images.objects.filter(user_id=user)[:1]
    context = {'user':user, 'user_images': user_images}
    return render(request, 'gaming/index.html', context)
  else:
    pass  

def fetch_level_based_data(request):
  
  level_images = {
    1 : ""
  }

  context = {
    'level_no' : 1,
    'grid_count' : 3,
    'level_images' : level_images
  }
  return render(request, 'gaming/level.html', context)

def user_login(request):
  context = RequestContext(request)
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse("Your Rango account is disabled.")
    else:
        print "Invalid login details: {0}, {1}".format(username, password)
        return HttpResponse("Invalid login details supplied.")
  else:
      return render(request, 'gaming/login.html', context)
