from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners of an object to access/edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user