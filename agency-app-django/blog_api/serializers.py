from rest_framework import serializers
from blog.models import Post
from rest_framework.reverse import reverse



class Post_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Post
        fields = ['url','id','headline','sub_headline','get_image_url','body','slug','publish_status','published','created','catagory','author']

    # def get_url(self, obj):

    #     return f"http://localhost:8000/blog/api/retrive-update/{obj.pk}/"


    def get_url(self, obj): 

        request = self.context.get('request') 

        if request is None:
            return None

        return reverse('blog:detail', kwargs={"pk": obj.pk, "slug":obj.slug}, request=request)







