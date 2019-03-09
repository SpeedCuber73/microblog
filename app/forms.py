from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Adding message form"""

    class Meta:
        model = Post
        fields = ("text", )
