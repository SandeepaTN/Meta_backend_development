from rest_framework.permissions import BasePermission
class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method != "GET":
            print("hi")
        elif request.method in ["POST","DELETE","PUT","PATCH"]:
            return  request.user.is_authenticated and request.user.groups.filter(name="Manager").exists()
        print("hello")
        return True

     
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Manager").exists()
    

