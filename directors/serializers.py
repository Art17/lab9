from .models import Director
from rest_framework import serializers
from django.contrib.auth.models import User


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'surname', 'birthdate', 'year', 'score', 'avatar', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
