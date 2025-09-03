# DjangoPracticeApp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView    # CBVs for CRUD
from django.urls import reverse_lazy                                # For success_url redirects
from .models import Task                                            # Our Task model


class TaskListView(ListView):
    """
    Displays a list of all tasks.
    """
    model = Task
    template_name = "DjangoPracticeApp/task_list.html"  # Which template to use
    context_object_name = "tasks"                      # Template variable name
    ordering = ["-created_at"]                         # Show newest tasks first


class TaskCreateView(CreateView):
    """
    Create a new Task.
    """
    model = Task
    fields = ["title", "completed"]                   # Which fields to show in form
    template_name = "DjangoPracticeApp/task_form.html" # Reuse task_form.html
    success_url = reverse_lazy("task_list")            # Redirect after success


class TaskUpdateView(UpdateView):
    """
    Edit an existing Task.
    """
    model = Task
    fields = ["title", "completed"]
    template_name = "DjangoPracticeApp/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    """
    Delete an existing Task.
    """
    model = Task
    template_name = "DjangoPracticeApp/task_confirm_delete.html"  # Confirmation page
    success_url = reverse_lazy("task_list")                       # Redirect after deletion
