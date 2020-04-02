from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        # exclude = [] # => 사용을 추천하지는 않음.
        fields = [
            'message', 'photo', 'tag_set', 'is_public'
        ]