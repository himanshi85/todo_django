from django.urls import path
from .views import ToDoListCreateView, ToDoDetailView

urlpatterns = [
    path('todos/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<uuid:todo_id>/', ToDoDetailView.as_view(), name='todo-detail'),
]
