from django.urls import path
from .views import (
    PostListCreateView,
    post_detail,
    create_post,
    add_comment,
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('create/', create_post, name='create-post'),
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:post_id>/comments/new/', add_comment, name='add-comment'),
]
