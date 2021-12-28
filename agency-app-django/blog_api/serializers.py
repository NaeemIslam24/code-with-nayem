from rest_framework import serializers
from blog.models import Post

class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'