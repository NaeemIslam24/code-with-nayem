# from rest_framework import generics
# from portfolio.models import Portfolio
# from . serializers import Portfolio_serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class List(generics.ListAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = Portfolio_serializer


# class Retrive(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = Portfolio_serializer
#     lookup_fields = [ "title", "pk"]



# # class Category(APIView):

# #     def get(self, request, formant=None):

# #         # # print('catagory...........', catagory)
# #         # test = request.user.id
# #         # print('test...........', test)

# #         category = request.GET['category']


# #         queryset = Portfolio.objects.filter(catagory = category)
        
# #         serializers = Portfolio_serializer(queryset, many=True)

# #         return Response(serializers.data)


# class Category(generics.ListAPIView):

#     queryset = Portfolio.objects.all()


#     def list(self, request):
       
#         category = request.GET['category']
#         queryset = self.get_queryset().filter(catagory=category)
#         serializer = Portfolio_serializer(queryset, many=True)
      
#         return Response(serializer.data)
    


from rest_framework import generics
from portfolio.models import Portfolio
from .serializers import  Portfolio_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response


class List(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_Serializer


class Retrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_Serializer
    lookup_fields = ["title", "pk"]


class Category(APIView):

    def get(self, request, formant=None):
        category = request.query_params.get('category')
        queryset = Portfolio.objects.filter(catagory=category)
        serializers = Portfolio_Serializer(queryset, many=True, context={'request': request})

        return Response(serializers.data)

# class Category(generics.ListAPIView):

#     lookup_fields =  "catagory"

#     queryset = Portfolio.objects.all()
#     serializer_class = Portfolio_serializer

    

        
