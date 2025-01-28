from rest_framework.permissions import DjangoModelPermissions

class CustomDjangoModelPermissions(DjangoModelPermissions):
    """
    Niestandardowe uprawnienia Django Model Permissions
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return super().has_permission(request, view)
        return False
