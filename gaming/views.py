from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
#from gaming.models import MyModel   # Import the model classes we just wrote.

def index(request):
    #latest_question_list = MyModel.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context = {'latest_question_list': "adasdasdas"}
    return render(request, 'gaming/index.html', context)
=======

def fetch_level_based_data:
  

    
>>>>>>> 1f7ce8b3bedd998bf85664221d3fd1188f71b1d8
