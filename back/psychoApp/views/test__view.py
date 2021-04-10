from ..models import TemplateTest
from rest_framework import viewsets

from ..serializers import TemplateTestSerializer
from ..serializers import BasicTemplateTestSerializer


class Test(viewsets.ModelViewSet):

    queryset = TemplateTest.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TemplateTestSerializer
        else:
            return BasicTemplateTestSerializer

    def get_queryset(self):
        queryset = TemplateTest.objects.all()

        name = self.request.query_params.get("name")
        concept = self.request.query_params.get("concept")

        if name is not None:
            queryset = queryset.filter(name=name)

        if concept is not None:
            queryset = queryset.filter(concept__icontains=concept)

        return queryset
