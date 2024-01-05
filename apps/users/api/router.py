from django.urls import path
from .views import (
    username_available,
    email_available,
    get_all_users,
    get_active_users,
    superadmin_get_all_users,
    user_detail_view,
    login_view,
    refresh_token_view,
    check_session,
    logout_view,
    user_request_view,
    groups_view,
)


urlpatterns = [
    # Available
    path(
        'users/check_username/<str:username>/',
        username_available,
        name='available_username_api'
    ),
    path(
        'users/check_email/<str:email>/',
        email_available,
        name='available_email_api'
    ),
    # Token
    path('users/token/', login_view, name='get-token'),
    path('users/token/logout/', logout_view, name='logout-token'),
    path(
        'users/token/refresh/',
        refresh_token_view,
        name='refresh-token'
    ),
    path(
        'users/check_session/',
        check_session,
        name='check-session'
    ),
    # Api
    path(
        'users/get_all_groups/',
        groups_view,
        name='get_all_groups_api'
    ),
    path(
        'users/superadmin/get_all_users/',
        superadmin_get_all_users,
        name='superadmin_get_all_users_api'
    ),
    path(
        'users/get_all_users/',
        get_all_users,
        name='get_all_users_api'
    ),
    path(
        'users/get_active_users/',
        get_active_users,
        name='get_active_users_api'
    ),
    path(
        'users/create_user/',
        user_detail_view,
        name='create_user_api'
    ),
    path(
        'users/detail_user/<int:pk>/',
        user_detail_view,
        name='detail_user_api'
    ),
    path(
        'users/update_user/<int:pk>/',
        user_detail_view,
        name='update_user_api'
    ),
    path(
        'users/delete_user/<int:pk>/',
        user_detail_view,
        name='delete_user_api'
    ),
    path(
        'users/purge_user/<int:pk>/',
        user_detail_view,
        name='purge_user_api'
    ),
    path(
        'users/request_user/',
        user_request_view,
        name='request_user_api'
    ),
]
