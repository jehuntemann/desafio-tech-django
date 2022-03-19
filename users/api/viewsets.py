from rest_framework import viewsets
from users.api import serializers
from users import models

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset =  models.User.objects.all()
    http_method_names = ["get"]

class UsersViewCreate(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    http_method_names = ["post"]