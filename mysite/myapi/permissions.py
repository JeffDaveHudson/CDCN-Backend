from rest_framework import permissions


class StaffAndUserPermission(permissions.BasePermission):

    staff_only = ("PUT", "PATCH", "POST", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_staff or request.method not in self.staff_only:
                return True
        return False
