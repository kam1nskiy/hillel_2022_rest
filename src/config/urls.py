from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import include, path


def check(request):
    data = {"nameee": "Vova"}
    # return HttpResponse('Hello')
    return JsonResponse(data)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check", check),
    path("posts/", include("posts.urls")),
]
