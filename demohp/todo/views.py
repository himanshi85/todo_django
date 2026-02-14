from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import ToDoSerializer
from django.shortcuts import get_object_or_404

class ToDoListCreateView(APIView):
    def get(self, request):
        todos = ToDo.objects.all().order_by('-created_at')
        serializer = ToDoSerializer(todos, many=True)
        return Response({
            'message': 'ToDo list fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'ToDo added successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Validation failed',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailView(APIView):
    def get_object(self, todo_id):
        return get_object_or_404(ToDo, todo_id=todo_id)

    def put(self, request, todo_id):
        todo = self.get_object(todo_id)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'ToDo updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Validation failed',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, todo_id):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response({
            'message': 'ToDo deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


    def post(self, request, todo_id):
        todo = self.get_object(todo_id)
        todo.completed = not todo.completed
        todo.save()
        return Response({
            'message': f"ToDo marked as {'completed' if todo.completed else 'pending'} successfully",
            'completed': todo.completed
        }, status=status.HTTP_200_OK)
