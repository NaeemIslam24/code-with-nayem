from blog.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .serializers import Post_serializer

class Post_api(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_serializer


class Post_detail(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_serializer



