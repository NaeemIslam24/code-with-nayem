from rest_framework import serializers
from blog.models import Post



class Post_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Post
        fields = ['url','id','headline','sub_headline','get_image_url','body','slug','publish_status','published','created','catagory','author']

    def get_url(self, obj):

        return f"http://localhost:8000/blog/api/retrive-update/{obj.pk}/"







