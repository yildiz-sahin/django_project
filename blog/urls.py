from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView,
                    CommentDetailView, CommentCreateView, CommentListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/all/', CommentListView.as_view(), name='comment-list'),
]
