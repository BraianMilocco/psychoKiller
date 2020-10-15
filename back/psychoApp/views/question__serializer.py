from ..models import Question
from rest_framework import viewsets

from ..serializers import QuestionSerializer 


class Questions(viewsets.ModelViewSet):

    queryset = Question.objects.all()   
    serializer_class = QuestionSerializer
    