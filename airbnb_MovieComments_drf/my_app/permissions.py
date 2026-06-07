from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'owner'


class IsGuest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'guest'

class CheckAdminRoleReviews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return False
        return True