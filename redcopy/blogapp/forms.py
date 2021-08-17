from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(ModelForm):
    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Empty Title")

    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'input is-normal', 'maxlength':"10",'placeholder': 'Post Title '}),
            'text': TinyMCE(attrs={"class": "textarea", "placeholder": "Add Post Text here "}),
        }


class EditForm(ModelForm):
    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Empty Title")

    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'Post Title '}),
            'text': TinyMCE(attrs={"class": "textarea", "placeholder": "Add Post Text here "}),
        }
