import pkg_resources
from rest_framework import serializers
from rest_framework.reverse import reverse
from portfolio.models import Portfolio, Category


class Portfolio_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Portfolio
        fields = ['url','title', 'client_name', 'project_date', 
        'Project_url', 'image1', 'image2', 'image3', 
        'image4','description', 'catagory']
    
    def get_url(self, obj): 

        request = self.context.get('request') 

        if request is None:
            return None

        return reverse("retrive", kwargs={"title": obj.title, "pk": obj.pk}, request=request)



    