# DjangoPracticeApp/urls.py

from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),       # List tasks
    path('add/', TaskCreateView.as_view(), name='task_add'),  # Add task
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),  # Edit task
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),  # Delete task

]
