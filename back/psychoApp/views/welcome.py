from django.http import JsonResponse


def welcome(request):
    hi = {"hello": "world"}

    return JsonResponse(hi)
