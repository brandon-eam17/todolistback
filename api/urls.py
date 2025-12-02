from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todo', todo_list, name='todo-list-create'),
    path('todos/<int:pk>/', todo_detail, name='todo-detail')
    
]