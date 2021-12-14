from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerialzer
from .models import Book

from .permissions import IsAuthenticatedOrReadOnly

# CR views
class BookList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerialzer

# RUD view
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# class PostCreate():
#     pass

# class PostUpdate():
#     pass

# class PostDelete():
#     pass