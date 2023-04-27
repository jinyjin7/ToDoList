from django.urls import path,include
from todo import views


urlpatterns = [
    path('',views.ToDoView.as_view(), name="todo_view"),

]
