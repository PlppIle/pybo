from django.shortcuts import render
from .models import Profile

def index(request):
    return render(request, 'portfolio/main.html')

def who(request):
    return render(request, 'portfolio/profile.html')

def where(request):
    return render(request, 'portfolio/hometown.html')

def what(request):
    return render(request, 'portfolio/ability.html')