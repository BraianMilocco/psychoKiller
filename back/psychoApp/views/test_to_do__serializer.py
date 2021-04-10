from ..models import TemplateTest
from rest_framework import viewsets

from ..serializers import TemplateTestSerializer


class Test_to_do(viewsets.ModelViewSet):

    queryset = TemplateTest.objects.all()
    serializer_class = TemplateTestSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = TemplateTest.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset