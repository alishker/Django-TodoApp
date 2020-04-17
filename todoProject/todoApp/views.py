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


def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)

    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todoApp/update_task.html', context)


def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todoApp/delete.html', context)
