from distutils.sysconfig import EXEC_PREFIX
from http.client import BAD_REQUEST
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer, UserLoginSerializer, UserSerializer, GenreSerializer, RatingSerializer, UserRegisterSerializer
from myapi import models
from rest_framework.decorators import action, api_view, permission_classes
import string
import random
from django.contrib.auth import authenticate, login, logout, hashers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
import json
from django.db.models import Avg, Count
import math
from myapi import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from myapi.permissions import StaffAndUserPermission
import pandas as pd

class BookManage(APIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        book_model = models.Book.objects
        try:
            if "id" in request.query_params:
                book_model = book_model.filter(
                    id=request.query_params["id"])
            if "title" in request.query_params:
                book_model = book_model.filter(
                    title__contains=request.query_params["title"])
            if "genre_id" in request.query_params:
                book_model = book_model.filter(
                    genre__id=request.query_params["genre_id"])
            if "page" in request.query_params and "pagesize" in request.query_params:
                pagesize = int(request.query_params["pagesize"])
                offset = (int(request.query_params["page"]) - 1) * pagesize
                book_model = book_model.all()[offset:offset+pagesize]
            serializer = BookSerializer(book_model, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RatingManage(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    serializer_class = RatingSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            rating_obj = models.Rating.objects.get(pk=pk)

            serializer = RatingSerializer(rating_obj)
        else:

            queryset = models.Rating.objects.all()
            serializer = RatingSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = get_object_or_404(models.Rating, pk=pk)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

    def put(self, request, pk, format=None):
        rating_obj = models.Rating.objects.get(pk=pk)
        serializer = RatingSerializer(data=request.data, instance=rating_obj)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Data updated successfully !!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        rating_obj = models.Rating.objects.get(pk=pk)
        serializer = RatingSerializer(
            data=request.data, instance=rating_obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Data updated successfully !!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)