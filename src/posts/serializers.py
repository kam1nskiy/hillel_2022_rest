from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("id", "created_at", "updated_at")