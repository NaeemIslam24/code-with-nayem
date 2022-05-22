from django.db import models

class Count(models.Model):

    number = models.CharField(max_length=10)
    subtitle = models.CharField(max_length=100)
    shorttext = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    def __str__(self):
        return self.number

        
class Testimonial1(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=264)
    def __str__(self):
        return self.title


class Testimonial2(models.Model):


    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='testimonials')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=264)
    def __str__(self):
        return self.name

class Client(models.Model):


    title = models.CharField(max_length=264)
    text = models.TextField(max_length=500)
    img1 = models.ImageField(upload_to='clients/')
    img2 = models.ImageField(upload_to='clients/')
    img3 = models.ImageField(upload_to='clients/')
    img4 = models.ImageField(upload_to='clients/')
    img5 = models.ImageField(upload_to='clients/')
    img6 = models.ImageField(upload_to='clients/')
    img7 = models.ImageField(upload_to='clients/')
    img8 = models.ImageField(upload_to='clients/')
    img9 = models.ImageField(upload_to='clients/')
    img10 = models.ImageField(upload_to='clients/')
    def __str__(self):
        return self.title

class About(models.Model):

  
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=264)
    text1 = models.TextField(max_length=1000)
    text2 = models.TextField(max_length=1000)
    def __str__(self):
        return self.title




