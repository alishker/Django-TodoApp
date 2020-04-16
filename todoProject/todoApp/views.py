from django.shortcuts import render
from .models import Tasks

# Create your views here.


def index(request):
    task = Tasks.objects.all()

    context = {'task': task}
    return render(request, 'todoApp/list.html', context)
