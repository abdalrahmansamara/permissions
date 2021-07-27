from rest_framework import serializers

from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'time_to_prepare', 'serving', 'ingredients', 'instructions','posted_by','created_at')
        model = Post