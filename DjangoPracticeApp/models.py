from django.db import models
# Import Django's model system (used to define database tables as Python classes)

class Task(models.Model):
    # Define a new database table called "Task" (Django creates this automatically)

    title = models.CharField(max_length=200)
    # A text field for the task title (max length 200 characters)

    completed = models.BooleanField(default=False)
    # A True/False field to mark whether the task is done (default = False)

    created_at = models.DateTimeField(auto_now_add=True)
    # A date & time field that automatically stores the time when the task was created

    def __str__(self):
        # This function defines how the object will be shown as a string
        return self.title
        # Example: instead of "Task object (1)", it will show the task title in admin or shell
