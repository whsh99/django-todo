# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

# Create your views here.
def todo(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # Print the retrieved task queryset to the console
    # print(tasks)

    completed_tasks = Task.objects.filter(is_completed=True)
    #print(completed_tasks)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'todo.html', context)