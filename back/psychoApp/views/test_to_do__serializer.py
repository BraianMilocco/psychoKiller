from ..models import TemplateTest
from rest_framework import viewsets

from ..serializers import TemplateTestSerializer


class Test_to_do(viewsets.ModelViewSet):

    queryset = TemplateTest.objects.all()
    serializer_class = TemplateTestSerializer
