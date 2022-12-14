from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer with fields to controll displayed fields
    fields: username, first_name, last_name, email,password
    """

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]
