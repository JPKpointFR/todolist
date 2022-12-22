from django.shortcuts import render
from .forms import TaskForm
from .models import Task


def create_task(request):
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        list = Task.objects.all()
        context = {
            'form': form,
            'tasks': list,
        }
        if form.is_valid():
            form.save()
    return render(request, 'tache/tache.html', context)
