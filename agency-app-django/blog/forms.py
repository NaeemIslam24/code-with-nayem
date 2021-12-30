from .models import *
from django import forms

class ModelPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "comment")
