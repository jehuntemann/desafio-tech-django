from operator import length_hint
from xml.etree.ElementTree import TreeBuilder
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

def random_password(): 
    return User.objects.make_random_password(length=30)

class Users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=10)
    password = models.CharField(max_length=30, default=random_password())
