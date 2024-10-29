# myapp/views.py

from django.shortcuts import render

def homepage(request):
    return render(request, 'myapp/homepage.html')  # Ensure this matches your template's path
