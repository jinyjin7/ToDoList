from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from todo.models import ToDoList
from todo.serializers import ToDoListSerializer,ToDoListCreateSerializer


# Create your views here.
class ToDoView(APIView):
    def get(self, request):
        todolists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #게시글만드는 코드
    def post(self, request):
        serializer = ToDoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
