
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path, include


def check (request):
    data = {"name" : "Vova"}
    # return HttpResponse('Hello')
    return JsonResponse(data)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health-check', check),
    path('posts/', include("posts.urls")),
]
