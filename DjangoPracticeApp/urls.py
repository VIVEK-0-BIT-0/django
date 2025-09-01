# DjangoPracticeApp/urls.py

from django.urls import path                # Import Django's path() for URL routing
from . import views                         # Import our views.py file

urlpatterns = [
    # When someone visits / (root of this app), call the task_list view.
    path('', views.task_list, name='task_list'),
]
