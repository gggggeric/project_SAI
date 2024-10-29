# myapp/urls.py

from django.urls import path
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),  # Map the root URL to the homepage view
]
