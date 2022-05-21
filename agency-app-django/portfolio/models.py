from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
      self.name = self.name.lower()
      return super(Category, self).save(*args, **kwargs)


class Portfolio(models.Model):

    catagory = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    client_name = models.CharField(max_length=50)
    project_date = models.DateTimeField(default=timezone.now)
    Project_url = models.URLField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to='',)
    image2 = models.ImageField(upload_to='', null=True, blank=True)
    image3 = models.ImageField(upload_to='', null=True, blank=True)
    image4 = models.ImageField(upload_to='', null=True, blank=True)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.client_name
