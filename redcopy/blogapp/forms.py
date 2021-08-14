from django.forms import TextInput
from tinymce.widgets import TinyMCE

from django import forms

from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'Post Title '}),
            'text': TinyMCE(attrs={'class': 'input'}),
        }
