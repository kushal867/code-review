from rest_framework import generics
from .models import CodePost, Comment
from .serializers import CodePostSerializer, CommentSerializer

class CodePostListCreateAPIView(generics.ListCreateAPIView):
    queryset = CodePost.objects.all().order_by('-created_at')
    serializer_class = CodePostSerializer

class CodePostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CodePost.objects.all()
    serializer_class = CodePostSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
