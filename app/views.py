from django.shortcuts import render , redirect
from django.http import HttpResponse
from app.models import Task

# Create your views here.
def addtask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('todohome')

def mark_as_done(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('todohome')


def mark_as_undo(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('todohome')


def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('todohome')