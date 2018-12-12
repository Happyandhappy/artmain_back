from django.contrib.auth import get_user_model
from rest_framework import permissions
User = get_user_model()

class TenantAdminPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """
    message = 'Access not allowed.'

    def has_permission(self, request, view):
        tenant = request.tenant
        email = request.META['HTTP_EMAIL']
        if User.objects.filter(email=email, tenant=tenant).first():
            return True
        else:
            return False


