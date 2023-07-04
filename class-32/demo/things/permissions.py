from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request,view, obj):
        if request.method == 'GET':
            return True
        if request.user == obj.owner:
            return True
        else:
            return False