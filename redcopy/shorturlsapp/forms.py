from django.forms import ModelForm, TextInput

from .models import ShortLinks
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    def clean(self, *args, **kwargs):
        origin_url = self.cleaned_data.get('origin_url')
        if not origin_url:
            raise ValidationError("Empty URL")

    class Meta:
        model = ShortLinks
        fields = ['origin_url']
        widgets = {
            'origin_url': TextInput(attrs={'class': 'input', 'placeholder': 'paste valid URL'}),
        }
