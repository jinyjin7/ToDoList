from rest_framework import serializers
from todo.models import ToDoList
from users.models import UserManager



class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    #이메일을 받아오기위한 변수작업
    
    class Meta:
        model = ToDoList
        fields='__all__'

class ToDoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields=("title","is_complete")
