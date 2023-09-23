from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # check if the user  is requesting read-only access and return True  
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Otherwise, we’ll return True only if the  user making the request owns the profile
        return obj.owner == request.user


class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.asset_id.project_id.owner == request.user:
            return obj.owner == request.user
        return False
        # def get_object(self, pk):
        # try:
        #     project = Profile.objects.get(pk=pk)
        #     self.check_object_permissions(self.request, profile)
        #     return profile
        # except Profile.DoesNotExist:
        #     raise Http404

        # check if the user  is requesting read-only access and return True  
        # if request.method in permissions.SAFE_METHODS:
        #     return True
            
        # Otherwise, we’ll return True only if the  user making the request owns the profile
        # return obj.owner == request.user

