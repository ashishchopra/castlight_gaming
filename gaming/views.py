from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from gaming.models import User_Images
from django.contrib.auth.models import User
# Import the model classes we just wrote.

import random

def index(request):
    user_images = User_Images.objects.all()
    context = {'user_images': user_images}
    return render(request, 'gaming/index.html', context)

def show_random_user_profile(request):
	users_count = User.objects.count()
	n = random.randint(1,users_count)
	user = User.objects.filter(id=n)[0]	
	if user:
	  user_images = User_Images.objects.filter(user_id=user)[:1]
	  context = {'user':user, user_images': user_images}
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
