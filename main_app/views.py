from django.shortcuts import render
from .models import Swallow

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def swallows_index(request):
  swallows = Swallow.objects.all()
  return render(request, 'swallows/index.html', {'swallows':swallows})

def swallows_detail(request, swallow_id):
  swallow = Swallow.objects.get(id=swallow_id)
  return render(request, 'swallows/detail.html', { 'swallow': swallow })
