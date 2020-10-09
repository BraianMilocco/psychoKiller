from django.http import JsonResponse
from django.core import serializers


def test_to_do(request, id):
    hi = {"hello": "world 2"}

    return JsonResponse(hi)
