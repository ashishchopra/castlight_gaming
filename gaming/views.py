from django.shortcuts import render

# Create your views here.
#from gaming.models import MyModel   # Import the model classes we just wrote.

def index(request):
    #latest_question_list = MyModel.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context = {'latest_question_list': "adasdasdas"}
    return render(request, 'gaming/index.html', context)

