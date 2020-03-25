from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    picture = forms.ImageField(required = False)
    class Meta:
        model = Post
        fields = ('title', 'text', 'picture',)
