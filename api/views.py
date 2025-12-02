from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer

@api_view({'GET', 'POST'})
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        todos = Todo.objects.all()
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view({'GET', 'PUT', 'DELETE'})
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)