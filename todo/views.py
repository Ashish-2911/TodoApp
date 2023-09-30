# myapp/views.py
from django.shortcuts import render
from app.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated')
    completed_task = Task.objects.filter(is_completed=True)
    lenght_complete_task = len(completed_task)
    context = {
        'tasks':tasks,
        'completed_task':completed_task,
        'lenght_complete_task':lenght_complete_task
    }
    return render(request, 'home.html', context)
