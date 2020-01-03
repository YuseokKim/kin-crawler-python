from django.db import models

# Create your models here.

class Device(models.Model):
    fcm_token = models.CharField(max_length=200)
    model = models.CharField(max_length=20)