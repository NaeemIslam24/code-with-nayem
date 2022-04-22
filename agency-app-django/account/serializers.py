from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth.models import User


# class Profile_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
=======
from . models import Profile
from django.contrib.auth.models import User

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83
