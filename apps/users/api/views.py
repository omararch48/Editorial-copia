from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from apps.users.models import User
from .serializers import (
    GroupSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserRequestSerializer,
)
from .permissions import AdminPermission


# Token, sessions
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')
    user = authenticate(email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        if not user.is_active:
            return Response(
               {'error': 'Email or password incorrect'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        login(request, user)
        if user.is_staff:
            session_key = request.session.session_key
            response = Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user_id': user.id,
                'username': user.username,
                'is_active': user.is_active,
                'is_staff': user.is_staff,
                'gender': user.gender,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'image': user.image,
                'gender': user.gender,
                'message': 'Login successful',
                # 'sessionid': session_key,
            }, status=status.HTTP_200_OK)
            # response.set_cookie('sessionid', session_key, max_age=None, secure=False, httponly=True)
            return response
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id,
            'username': user.username,
            'is_active': user.is_active,
            'gender': user.gender,
            'message': 'Login successful',
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'Email or password incorrect'},
            status=status.HTTP_200_OK
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    try:
        # token = request.headers['Authorization'].replace('Bearer ', '')
        # user_id = -1
        # decoded_token = AccessToken(token)
        # user_id = decoded_token['user_id']
        refresh = RefreshToken(request.data['refresh'])
        access_token = str(refresh.access_token)
        user = User.objects.get(pk=request.data['id'])
        # if user_id == refresh['user_id']:
        return Response(
            {
                'access': access_token,
                'user_id': user.id,
                'username': user.username,
                'is_active': user.is_active,
                'is_staff': user.is_staff,
                'gender': user.gender,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'image': user.image,
                'gender': user.gender,
                'message': 'Login successful',
            },
            status=status.HTTP_200_OK
        )
        # return Response(
        #     {'error': 'Error al refrescar el token'},
        #     status=status.HTTP_400_BAD_REQUEST
        # )
    except Exception as e:
        return Response(
            {'error': 'Error al refrescar el token'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh = RefreshToken(request.data['refresh'])
        refresh.blacklist()
        logout(request)
        return Response(
            {'message': 'logout successful'}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {'message': 'logout failed'},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def check_session(request):
    token = request.headers['Authorization'].replace('Bearer ', '')
    user_id = -1
    try:
        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']
    except Exception as e:
        user_id = -1
    if request.data['id'] == user_id:
        return Response({"session": True,}, status.HTTP_200_OK)
    return Response({"session": False,}, status.HTTP_200_OK)


# Api
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def groups_view(request):
    groups = Group.objects.all()
    if groups:
        groups_serializer = GroupSerializer(groups, many=True)
        return Response(groups_serializer.data, status.HTTP_200_OK)
    return Response({'message': 'Groups not foud'}, status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def username_available(request, username=''):
    user = User.objects.filter(username=username)
    username_available = True
    if len(user) > 0:
        username_available = False
    return Response(
        {'username_available': username_available},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def email_available(request, email=''):
    email = User.objects.filter(email=email)
    email_available = True
    if len(email) > 0:
        email_available = False
    return Response(
        {'email_available': email_available},
        status=status.HTTP_200_OK
    )


@api_view(['GET',])
@permission_classes([AdminPermission])
def superadmin_get_all_users(request):
    users = User.objects.all()
    if users:
        users_serializer = UserListSerializer(
            users,
            many=True,
            context={'request_user': request.user}
        )
        return Response(users_serializer.data, status.HTTP_200_OK)
    return Response({'message': 'Users not foud'}, status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
@permission_classes([AdminPermission])
def get_all_users(request):
    users = User.objects.all()
    if users:
        users_serializer = UserListSerializer(
            users,
            many=True,
            context={'request_user': request.user}
        )
        return Response(users_serializer.data, status.HTTP_200_OK)
    return Response({'message': 'Users not foud'}, status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def get_active_users(request):
    active_users = User.objects.filter(is_active=True)
    if active_users:
        users_serializer = UserListSerializer(
            active_users,
            many=True,
            context={'request_user': request.user}
        )
        return Response(users_serializer.data, status.HTTP_200_OK)
    return Response(
        {'message': 'No active users not foud'},
        status.HTTP_404_NOT_FOUND
    )


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE',])
@permission_classes([IsAuthenticated])
def user_detail_view(request, pk=None):
    try:
        if request.method != 'POST':
            user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(
            {'message': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        if user.is_staff:
            user_serializer = UserDetailSerializer(user)
            return Response(user_serializer.data, status.HTTP_200_OK)
        else:
            user_serializer = UserListSerializer(
                user,
                many=False,
                context={'request_user': request.user}
            )
            return Response(user_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        user_serializer = UserDetailSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status.HTTP_201_CREATED)
        return Response(
            {'message': 'data not valid'},
            status.HTTP_406_NOT_ACCEPTABLE
        )
    elif request.method in ['PUT', 'PATCH',]:
        if 'username' in request.data:
            user.username = request.data['username']
        if 'first_name' in request.data:
            user.first_name = request.data['first_name']
        if 'last_name' in request.data:
            user.last_name = request.data['last_name']
        if 'email' in request.data:
            user.email = request.data['email']
        if 'gender' in request.data:
            user.gender = request.data['gender']
        if 'image' in request.data:
            user.image = request.data['image']
        if 'status' in request.data:
            user.status = request.data['status']
        if 'is_active' in request.data:
            user.is_active = request.data['is_active']
        if 'is_staff' in request.data:
            user.is_staff = request.data['is_staff']
        if 'is_student' in request.data:
            user.is_student = request.data['is_student']
        if 'is_teacher' in request.data:
            user.is_teacher = request.data['is_teacher']
        if 'is_superuser' in request.data:
            user.is_superuser = request.data['is_superuser']
        if 'password' in request.data:
            user.set_password(request.data['password'])
        user.save()
        user_serializer = UserDetailSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'Eliminado',}, status.HTTP_200_OK)
    return Response(
        {'message': 'method not allowed'},
        status.HTTP_406_NOT_ACCEPTABLE
    )


@api_view(['POST',])
@permission_classes([AllowAny])
def user_request_view(request):
    user_serializer = UserRequestSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status.HTTP_201_CREATED)
    return Response(
        {'message': 'data not valid'},
        status.HTTP_406_NOT_ACCEPTABLE
    )