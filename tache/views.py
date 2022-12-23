from django.shortcuts import render, redirect, HttpResponse

from .models import Task
from .forms import TaskForm


def create_task(request):
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        list = Task.objects.all()
        context = {
            'form': form,
            'tasks': list,
        }
        if form.is_valid():
            form.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request, 'task.html', context)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update.html', {'form': form})


def delete_task(request, pk):
    Task.objects.filter(pk=pk).delete()

    return redirect('/task')
