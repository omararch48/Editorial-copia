from rest_framework import serializers
from django.contrib.auth.models import Group
from apps.users.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        exclude = ['permissions',]
        # fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'image',
            'status',
        ]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        request_user = self.context.get('request_user')
        if request_user.is_superuser:
            return super().to_representation(instance)
        # elif request_user:
        else: # permission
            if instance.is_active:
                return {
                    'id': instance.id,
                    'username': instance.username,
                    'email': instance.email,
                    'first_name': instance.first_name,
                    'last_name': instance.last_name,
                    'image': instance.image,
                    'gender': instance.gender,
                }
            return {
                'id': instance.id,
                'is_active': instance.is_active,
            }
        return {'message': 'user not found'}


class KeyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class UserDetailSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    is_active = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': instance.password,
            'email': instance.email,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'image': instance.image,
            'gender': instance.gender,
            'is_active': instance.is_active,
            'is_staff': instance.is_staff,
            'is_superuser': instance.is_superuser,
        }