from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)