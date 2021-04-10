from rest_framework import serializers
from ..models import TemplateTest
from .question_serializer import QuestionSerializer


class TemplateTestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = TemplateTest
        fields = ["name", "concept", "questions"]


class BasicTemplateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateTest
        fields = "__all__"  # ["name", "concept"]
