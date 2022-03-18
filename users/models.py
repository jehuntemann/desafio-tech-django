from django.db import models
from uuid import uuid4

# Create your models here.


class users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

