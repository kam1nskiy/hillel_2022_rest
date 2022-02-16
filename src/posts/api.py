from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from posts.serializers import PostSerializer

from .models import Post

class PostListCreateAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"