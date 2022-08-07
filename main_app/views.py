from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def swallows_index(request):
  return render(request, 'swallows/index.html', {'swallows':swallows})

class Swallow:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, age, speed):
    self.name = name
    self.breed = type
    self.description = description
    self.age = age
    self.speed = speed

swallows = [
  Swallow('Lolo', 'tabby', 'Kinda rude.', 3, 5),
  Swallow('Sachi', 'tortoiseshell', 'Looks like a turtle.', 5,5),
  Swallow('Fancy', 'bombay', 'Happy fluff ball.', 4,5),
  Swallow('Bonk', 'selkirk rex', 'Meows loudly.', 6,5)
]