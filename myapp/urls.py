from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    # path('', views.item_list, name='item_list'),
    # path('add/', views.item_create, name='item_create'),
    # path('edit/<int:id>/', views.item_update, name='item_update'),
    # path('delete/<int:id>/', views.item_delete, name='item_delete'),
]
