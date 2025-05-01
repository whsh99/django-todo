# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request, 'home.html')

def todo(request):
    return render(request, 'todo.html')