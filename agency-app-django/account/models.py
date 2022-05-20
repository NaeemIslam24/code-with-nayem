from django.db import models
from django.contrib.auth.models import User
import random

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    user_id_number = models.CharField(max_length=20)
    active_pro = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="user", default="user/user.png")
    bio = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    auth_token = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)

    

    def save(self, *args, **kwargs):
    
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(6):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.user_id_number = code_string
        super().save(*args, **kwargs)
    

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


