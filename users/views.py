from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer,CustomTokenObtainPairSerializer,UserProrileSerializer,UserProrileCorrectionSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView)
from users.models import User


# Create your views here.
class UserView(APIView):
    #회원가입
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"회원가입 성공!"},status=status.HTTP_201_CREATED)
        else:
            return Response({"massage":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProrileSerializer(user)
        return Response(serializer.data) 
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProrileCorrectionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        


#커스텀
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#로그인되어있는지 확인
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("get 요청")