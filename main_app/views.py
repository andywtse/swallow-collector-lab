from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Swallow, Item
from .forms import MigrationForm

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def swallows_index(request):
  swallows = Swallow.objects.filter(user=request.user)
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('swallows_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class SwallowCreate(LoginRequiredMixin,CreateView):
  model = Swallow
  fields = ['name', 'type', 'description', 'age', 'speed']
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class SwallowUpdate(LoginRequiredMixin,UpdateView):
  model = Swallow
  fields = ['type', 'description', 'age', 'speed']

class SwallowDelete(LoginRequiredMixin,DeleteView):
  model = Swallow
  success_url = '/swallows/'
  
class ItemCreate(LoginRequiredMixin,CreateView):
    model = Item
    fields = '__all__'
    
class ItemList(LoginRequiredMixin,ListView):
  model = Item
  
class ItemDetail(LoginRequiredMixin,DetailView):
  model = Item
  
class ItemUpdate(LoginRequiredMixin,UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(LoginRequiredMixin,DeleteView):
  model = Item
  success_url = '/items/'
