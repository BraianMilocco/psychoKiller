from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import TemplateTest
from ..serializers.templateTest_serializer import TemplateTestSerializer 


def test_to_do(request):
    templateTest = TemplateTest.objects.all()
    
    serializer = TemplateTestSerializer(templateTest, many=True)
    
    return JsonResponse(serializer.data, safe=False)
