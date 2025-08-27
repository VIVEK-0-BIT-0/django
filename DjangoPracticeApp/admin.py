from django.contrib import admin   # Import Django's admin interface
from .models import Task           # Import the Task model we created in models.py

# Register the Task model so it shows up in the Django admin dashboard
admin.site.register(Task)
