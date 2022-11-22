from django.db import models

class sync_immunization(models.Model):
    origin_url = models.CharField(max_length=255)
    etag = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)