from django.http import JsonResponse
from ..models import TemplateTest, Question


def welcome(request):
    hi = {"hello": "world"}

    return JsonResponse(hi)
