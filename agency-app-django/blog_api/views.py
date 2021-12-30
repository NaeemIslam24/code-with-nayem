from django.db.models import query

from django.http import request
from rest_framework.decorators import permission_classes
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission, SAFE_METHODS, DjangoModelPermissions
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView, get_object_or_404
# Create your views here.
from .serializers import Post_serializer
from rest_framework import serializers, viewsets
# #permissions keys
# IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,
# DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly





#custom permission for edit post. the user write the post will be caught
class PostUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# use of viewsets
class PostList(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()

    def list(self, request):
        serializer_class = Post_serializer(self.queryset, many = True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk = pk)
        serializer_class = Post_serializer(post)
        return Response(serializer_class.data)


# #model viewset
# class PostList(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = Post_serializer
#     queryset = Post.objects.all()


# class Post_api(ListCreateAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Post.objects.all()
#     serializer_class = Post_serializer


class Post_detail(RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = Post_serializer
