from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError


from .models import Post




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
            'text': Textarea(attrs={"class": "textarea", "placeholder": "Add Post Text here "}),
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
            'text': Textarea(attrs={"class": "textarea", "placeholder": "Add Post Text here "}),
        }
