from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User



#프로필보기
class UserProrileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("name","email","gender","age","bio")


#프로필수정
class UserProrileCorrectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("name", "password", "gender", "age", "bio")

    def update(self, instance, validated_data):
        # 비밀번호를 해싱하여 저장
        password = validated_data.get('password')
        instance.set_password(password)  # 비밀번호를 해싱하여 저장
        instance.name = validated_data.get('name')
        instance.gender = validated_data.get('gender')
        instance.age = validated_data.get('age')
        instance.bio = validated_data.get('bio')
        instance.save()
        return instance
        

#기본유저시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","email","password","gender","age","bio")

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self,instance, validated_data):
        user = super().update(instance, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

#jwt토큰 커스텀
# email, name, gender, age
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age
        
        return token