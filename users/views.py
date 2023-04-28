from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer,CustomTokenObtainPairSerializer,UserProrileSerializer
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

#유저프로필
class ProfileView(APIView):
    #프로필 보기
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProrileSerializer(user)
        return Response(serializer.data) 
    
    #프로필 수정 (2차)
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    #회원탈퇴
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = UserSerializer(user, data=request.data)
            user.delete()
            return Response({"회원탈퇴 완료!"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"권한이 없습니다"},status=status.HTTP_403)

#회원 로그아웃->로그인이안됨,,
class LogoutView(APIView):
    def post(self, request,user_id):
        user = get_object_or_404(User, id=user_id)
        response = Response({"로그아웃 성공!"}, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('refreshtoken')

        return response



#커스텀
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#로그인되어있는지 확인
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("로그인중!")