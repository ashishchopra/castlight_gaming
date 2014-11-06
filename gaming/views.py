from django.shortcuts import render
import random

# Create your views here.
from gaming.models import User_Images   # Import the model classes we just wrote.

level_grid = {
  1 : 9,
  2 : 16,
  3 : 25
}

def index(request):
    user_images = User_Images.objects.all()
    #context = {'latest_question_list': latest_question_list}
    context = {'user_images': user_images}
    return render(request, 'gaming/index.html', context)

def fetch_level_based_data(request):
  
  user_images = User_Images.objects.filter(user_id!=current_user)
  random_images_count = level_grid[level_no]
  level_images = random.sample(user_images, random_images_count)

  context = {
    'level_no' : 1,
    'grid_count' : 3,
    'level_images' : level_images
  }
  return render(request, 'gaming/level.html', context)
