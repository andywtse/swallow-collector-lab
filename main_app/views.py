from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Swallow, Item
from .forms import MigrationForm

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
  no_swallow_items = Item.objects.exclude(id__in = swallow.items.all().values_list('id'))
  migration_form = MigrationForm()
  return render(request, 'swallows/detail.html', { 'swallow': swallow, 'migration_form': migration_form, 'items': no_swallow_items })

def add_migration(request, swallow_id):
  form = MigrationForm(request.POST)
  if form.is_valid():
    new_migration = form.save(commit=False)
    new_migration.swallow_id = swallow_id
    new_migration.save()
  return redirect('swallows_detail', swallow_id=swallow_id)

def assoc_item(request, swallow_id, item_id):
  Swallow.objects.get(id=swallow_id).items.add(item_id)
  return redirect('swallows_detail', swallow_id=swallow_id)

class SwallowCreate(CreateView):
  model = Swallow
  fields = ['name', 'type', 'description', 'age', 'speed']
  success_url = '/swallows/'
  
class SwallowUpdate(UpdateView):
  model = Swallow
  fields = ['type', 'description', 'age', 'speed']

class SwallowDelete(DeleteView):
  model = Swallow
  success_url = '/swallows/'
  
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    
class ItemList(ListView):
  model = Item
  
class ItemDetail(DetailView):
  model = Item
  
class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'
