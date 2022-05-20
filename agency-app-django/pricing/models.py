from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Profile

import random

# Create your models here.
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField



class Plan_category(models.Model):

    plan_name = models.CharField(max_length=50)
    def __str__(self):
        return self.plan_name

class Banking_name(models.Model):
    banking_name = models.CharField(max_length=50)

    def __str__(self):
        return self.banking_name



class Purchasing(models.Model):

    profi = models.OneToOneField(Profile, on_delete = models.CASCADE, null=True, blank=True)
    plan_name = models.ForeignKey(Plan_category, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    banking_name = models.ForeignKey(Banking_name, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=60)
    number = models.CharField(max_length=20)
    How_much_you_paid = models.CharField(max_length=10, null=True, blank=True)
    active = models.BooleanField(default=False)
    requested_time = models.DateTimeField(default=timezone.now,null=True, blank=True)

    class Meta:
            ordering = ('-requested_time',) 
 
    def save(self, *args, **kwargs):
        username = str(get_current_authenticated_user())  
        self.user_name = username
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.user_name)


