# DjangoPracticeApp/views.py

from django.shortcuts import render           # Import render to use HTML templates
from .models import Task                      # Import Task model to fetch tasks from DB


def task_list(request):
    """
    View to fetch all tasks from the database and pass them to the template.
    """
    # Get all tasks from the database
    tasks = Task.objects.all()

    # Render the template and pass the tasks as context
    return render(request, 'DjangoPracticeApp/task_list.html', {'tasks': tasks})
