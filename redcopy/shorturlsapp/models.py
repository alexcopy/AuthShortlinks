from django.db import models
from django.conf import settings
from urllib.parse import urlparse
from django.core.exceptions import ValidationError


class ShortLinks(models.Model):
    def validate_url(url):
        if not url:
            return  # Required error is done the field
        parsed_url = urlparse(url)
        if not parsed_url.scheme in ['http', 'https', 'ftp', 'fttps']:
            raise ValidationError(' Please, check there only HTTP(S), and FTP(S) schemas are allowed!  ')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rnd_key = models.CharField(max_length=10, unique=True)
    origin_url = models.CharField(max_length=255, validators=[validate_url])
    is_disabled = models.PositiveSmallIntegerField(default=0)
    redirect_count = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
