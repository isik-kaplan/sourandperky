from contextlib import suppress

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        with suppress(AttributeError):
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return request.user == obj.owner
