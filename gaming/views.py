from django.shortcuts import render

# Create your views here.
from gaming.models import User_Images   # Import the model classes we just wrote.

def index(request):
    user_images = User_Images.objects.all()
    #context = {'latest_question_list': latest_question_list}
    context = {'user_images': user_images}
    return render(request, 'gaming/index.html', context)
