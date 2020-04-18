from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['photo', 'caption', 'location']
        widgets = {
            "caption": forms.Textarea,
        }