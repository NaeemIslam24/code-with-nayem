from rest_framework import generics
from portfolio.models import Portfolio, Category
from .serializers import  Portfolio_serializer
from rest_framework.views import APIView
from rest_framework.response import Response

class List(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_serializer


class Retrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_serializer
    lookup_fields = ["title", "pk"]

class Category(APIView):

    def get(self, request, formant=None):

        '''
        request.query_params.get('category') and request.GET['category'] both do same work

        '''
        # category = request.GET['category']
        category = request.query_params.get('category')

        queryset = Portfolio.objects.filter(catagory__name = category)

        # BY context={'request': request} we sent context to Portfolio_serializer
        serializers = Portfolio_serializer(queryset, many=True, context={'request': request})

        return Response(serializers.data)





    

        
