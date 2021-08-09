from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=280)
    text = models.TextField()
    slug = models.CharField(max_length=280)
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
