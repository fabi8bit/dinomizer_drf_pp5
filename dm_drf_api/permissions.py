from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # check if the user  is requesting read-only access and return True
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, we’ll return True only if
        # the user making the request owns the profile
        return obj.owner == request.user

        # check if the user is requesting
        # read-only access and return True
        # if request.method in permissions.SAFE_METHODS:
        # return True

        # Otherwise, we’ll return True only if the user
        # making the request owns the profile
        # return obj.owner == request.user


class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.asset_id.project_id.owner == request.user:
            return obj.asset_id.project_id.owner == request.user
        return False

        # this permission is used for checks.
        # check if the user is also the project owner otherwise it will return
        # false and denied the permission
