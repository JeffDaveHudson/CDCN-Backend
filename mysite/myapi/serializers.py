
from numpy import average
from myapi import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'photourl', 'genre', 'linkbook')
        depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('id', 'name')


class UserView(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username')


class RatingSerializer(serializers.ModelSerializer):
    user = UserView()
    book = BookSerializer()

    class Meta:
        model = models.Rating
        fields = ('id', 'user', 'book', 'rating')
