from django.shortcuts import render, redirect
from .models import Tasks
from .form import TodoForm

# Create your views here.


def index(request):
    task = Tasks.objects.all()

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task': task, 'form': form}
    return render(request, 'todoApp/list.html', context)
