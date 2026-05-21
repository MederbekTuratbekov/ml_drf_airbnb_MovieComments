from rest_framework import permissions


class CheckOwnerRoleReviews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'owner':
            return False
        return True

class CheckGuestRoleReviews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'guest':
            return False
        return True

class CheckAdminRoleReviews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return False
        return True