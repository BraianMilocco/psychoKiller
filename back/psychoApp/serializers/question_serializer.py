from rest_framework import serializers
from .option_serializer import OptionSerializer
from .templateTest_serializer import TemplateTestSerializer
from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    template = TemplateTestSerializer(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"  # ['number','query','options']
