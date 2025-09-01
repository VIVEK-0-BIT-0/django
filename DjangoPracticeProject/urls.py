# DjangoPracticeProject/urls.py

from django.contrib import admin               # Import Django’s admin site
from django.urls import path, include          # path = define URLs, include = include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),           # Enable Django admin at /admin/

    # Include your app's urls.py so requests get routed to your app.
    # '' means the app is served at the root (http://127.0.0.1:8000/).
    path('', include('DjangoPracticeApp.urls')),
]
