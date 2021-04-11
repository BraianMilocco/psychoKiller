from ..models import TemplateTest
from rest_framework import viewsets

from ..serializers import TemplateTestSerializer
from ..serializers import BasicTemplateTestSerializer


class Test_to_do(viewsets.ModelViewSet):

    queryset = TemplateTest.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
           
            return TemplateTestSerializer
        else:
            return BasicTemplateTestSerializer

    # serializer_class = get_serializer_class()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = TemplateTest.objects.all()
        name = self.request.query_params.get("name")
        concept = self.request.query_params.get("concept")
        include_questions = False
        if name is not None:
            queryset = queryset.filter(name=name)
        if concept is not None:
            queryset = queryset.filter(concept__icontains=concept)
        if not include_questions:
            queryset = queryset.defer("questions")
        return queryset
