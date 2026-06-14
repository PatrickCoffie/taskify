from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")

        if title:
            Task.objects.create(title=title, category=category)

    return redirect("home")

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("home")