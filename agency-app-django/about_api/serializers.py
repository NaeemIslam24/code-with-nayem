from rest_framework import serializers
from about.models import Testimonial1, Client, About, Count, Testimonial2



class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id','img','title','text1','text2']



class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','title','text','img1','img2','img3','img4','img5','img6','img7','img8','img9','img10']




class Count_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ['id','number','subtitle','shorttext','url']



class Testimonial1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial1
        fields = ['id','title','subtitle']

class Testimonial2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial2
        fields = ['id','name','img','title','text']

