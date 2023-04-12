from django import forms
from BlogApp.models import Post

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = '__all__'
        