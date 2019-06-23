from contextlib import suppress

from rest_framework import permissions


class IsOwnerOrDeny(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        with suppress(AttributeError):
            return request.user == obj.owner
