from rest_framework.permissions import BasePermission


class Mypermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type != 2:
            return False
        return True