from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.CodePostListCreateAPIView.as_view(), name='codepost-list-create'),
    path('posts/<int:pk>/', views.CodePostRetrieveAPIView.as_view(), name='codepost-detail'),
    path('comments/', views.CommentCreateAPIView.as_view(), name='comment-create'),
]
