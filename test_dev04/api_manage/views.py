from django.http import HttpResponse, JsonResponse


# Create your views here.

def debug(request):
    return JsonResponse({"code": 200, "msg": "true", "data": "12312312312"})
