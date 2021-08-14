from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=280)
    text = HTMLField()
    slug = models.SlugField()
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_view', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
