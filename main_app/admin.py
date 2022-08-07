from django.contrib import admin
from .models import Swallow, Migration, Item

# Register your models here.
admin.site.register(Swallow)
admin.site.register(Migration)
admin.site.register(Item)
