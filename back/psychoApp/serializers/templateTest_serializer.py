from rest_framework import serializers
from ..models import TemplateTest

class TemplateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateTest
        fields = ['name', 'concept']

