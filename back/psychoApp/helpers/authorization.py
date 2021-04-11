from rest_framework.permissions import IsAdminUser
# from rest_framework.permissions import 
# Function to know if the request method need permission
def should_check_permissions(method, *wargs):
    return method in wargs

# Permissions verification class
class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

# class IsLoggeed(IsAdminUser):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)