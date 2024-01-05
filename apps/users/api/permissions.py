from rest_framework.permissions import BasePermission
from modules.permissions.permissions_dict import perm_dict


APP_NAME = 'users'
APP_METHODS = {
    'get': 'get',
    'post': 'post',
    'update': 'update',
    'delete': 'delete',
}

class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        client_condition = request.user.is_staff and request.user.is_active
        client_condition = client_condition and (request.user.status == '0')
        GROUPS = request.user.groups.values_list(
            'name',
            flat = True
        )
        if perm_dict['super_admin'] in GROUPS:
            return True
        return False


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        admin_condition = request.user.is_staff and request.user.is_active
        admin_condition = admin_condition and (request.user.status == '0')
        GROUPS = request.user.groups.values_list(
            'name',
            flat = True
        )
        if perm_dict['super_admin'] in GROUPS:
            return True
        elif request.method == 'DELETE':
            return (
                (perm_dict[APP_METHODS['delete']] in GROUPS)
                and
                (perm_dict[APP_NAME] in GROUPS)
                and
                admin_condition
            )
        elif request.method == 'PUT' or request.method == 'PATCH':
            return (
                (perm_dict[APP_METHODS['update']] in GROUPS)
                and
                (perm_dict[APP_NAME] in GROUPS)
                and
                admin_condition
            )
        elif request.method == 'POST':
            return (
                (perm_dict['post'] in GROUPS)
                and
                (perm_dict[APP_NAME] in GROUPS)
                and
                admin_condition
            )
        elif request.method == 'GET':
            return (
                (perm_dict[APP_METHODS['get']] in GROUPS)
                and
                (perm_dict[APP_NAME] in GROUPS)
                and
                admin_condition
            )
        return False
