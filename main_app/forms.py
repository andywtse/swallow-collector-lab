from django.forms import ModelForm
from .models import Migration

class MigrationForm(ModelForm):
  class Meta:
    model = Migration
    fields = ['destination', 'rating']