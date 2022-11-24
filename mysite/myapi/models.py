from django.conf import settings
import time
from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    photourl = models.CharField(max_length=200)
    linkbook = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


# class Staff(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username


class User(AbstractUser):
    # Delete not use field
    last_login = None

    password = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through='Rating')
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


# keyword : Extra fields on many-to-many relationships
