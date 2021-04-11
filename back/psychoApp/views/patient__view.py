from ..models import Patient as Patient_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from ..serializers import PatientSerializer

from ..helpers import IsSuperUser
from ..helpers import should_check_permissions


@permission_classes([IsAuthenticated])
class Patient(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if should_check_permissions(self.action, 'retrieve'):
            
            return PatientSerializer
        else:
            return PatientSerializer

    def get_permissions(self):
        if should_check_permissions(self.request.method, 'POST','PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'): 
            self.permission_classes = [IsSuperUser]  

        return super(Patient, self).get_permissions()
        
    def get_queryset(self):
        queryset = Patient_model.objects.filter(therapist = self.request.user)
        # name = self.request.query_params.get("first_name")
        # lastname = self.request.query_params.get("last_name")

        # if name is not None:
        #     queryset = queryset.filter(concept__icontains=name)

        # if lastname is not None:
        #     queryset = queryset.filter(concept__icontains=lastname)

        return queryset