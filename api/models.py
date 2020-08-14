from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)