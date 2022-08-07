from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('swallows/', views.swallows_index, name='swallows_index'),
  path('swallows/<int:swallow_id>/', views.swallows_detail, name='swallows_detail'),
  path('swallows/create/', views.SwallowCreate.as_view(), name='swallows_create'),
  path('swallows/<int:pk>/update/', views.SwallowUpdate.as_view(), name='swallows_update'),
  path('swallows/<int:pk>/delete/', views.SwallowDelete.as_view(), name='swallows_delete'),
  path('swallows/<int:swallow_id>/add_migration/', views.add_migration, name='add_migration'),
  path('swallows/<int:swallow_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
  path('items/', views.ItemList.as_view(), name='items_index'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]