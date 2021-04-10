from rest_framework import serializers
from .option_serializer import OptionSerializer

from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"
