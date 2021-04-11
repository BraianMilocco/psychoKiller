from ..models import TemplateTest

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from ..serializers import TemplateTestSerializer
from ..serializers import BasicTemplateTestSerializer

from ..helpers import IsSuperUser
from ..helpers import should_check_permissions



@permission_classes([IsAuthenticated])
class Test(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if should_check_permissions(self.action, 'retrieve'):
            
            return TemplateTestSerializer
        else:
            return BasicTemplateTestSerializer

    def get_permissions(self):
        if should_check_permissions(self.request.method, 'POST','PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'): 
            self.permission_classes = [IsSuperUser]  

        return super(Test, self).get_permissions()
        
    def get_queryset(self):
        queryset = TemplateTest.objects.all()

        name = self.request.query_params.get("name")
        concept = self.request.query_params.get("concept")

        if name is not None:
            queryset = queryset.filter(name=name)

        if concept is not None:
            queryset = queryset.filter(concept__icontains=concept)

        return queryset


      