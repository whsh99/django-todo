from django.urls import path
from . import views

urlpatterns = [
    # Adding tasks
    path('addTask/', views.addTask, name='addTask'),
    # Marking tasks as done and undone
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Editing tasks
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Deleting tasks
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]