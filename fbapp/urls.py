# userinfo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('list-users/', views.list_users, name='list_users'),
    path('edit-user/<str:user_id>/', views.edit_user, name='edit_user'),  # NEW
    path('delete-user/<str:user_id>/', views.delete_user, name='delete_user'),  # NEW

]
