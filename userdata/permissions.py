from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
from rest_framework import status, exceptions


class authenticated_only(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            msg = {'status': status.HTTP_400_BAD_REQUEST,"message":"User account is disabled.",'error': True} 
            raise exceptions.AuthenticationFailed(msg)
        
        return request.method