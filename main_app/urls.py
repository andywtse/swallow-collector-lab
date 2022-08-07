from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('swallows/', views.swallows_index, name='swallows_index'),
  path('swallows/<int:swallow_id>/', views.swallows_detail, name='swallows_detail'),
]