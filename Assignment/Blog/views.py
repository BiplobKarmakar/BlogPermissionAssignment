from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class = PostSerializers

    


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    
    serializer_class = PostSerializers    
