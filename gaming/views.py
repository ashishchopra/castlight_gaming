from django.shortcuts import render

# Create your views here.
from gaming.models import User_Images   # Import the model classes we just wrote.

def index(request):
    user_images = User_Images.objects.all()
    #context = {'latest_question_list': latest_question_list}
    context = {'user_images': user_images}
    return render(request, 'gaming/index.html', context)

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
