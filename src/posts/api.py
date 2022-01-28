from django.http import JsonResponse


def posts():
    return JsonResponse({"results": []})