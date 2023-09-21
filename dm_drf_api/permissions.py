from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # check if the user  is requesting read-only access and return True  
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Otherwise, we’ll return True only if the  user making the request owns the profile
        return obj.owner == request.user

