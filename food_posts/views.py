from django.shortcuts import render
from .serializer import PostsSerializer
from .models import Post
# Create your views here.
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class PostsListView(generics.ListCreateAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)