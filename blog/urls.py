from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('posts/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Post detail
    path('post/new/', views.create_post, name='create_post'),  # Create a new post
    path('post/<int:pk>/edit/', views.update_post, name='update_post'),  # Update post
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),  # Delete post
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),  # Filter by tag

    # Comments
    path('post/<int:pk>/comment/new/', views.add_comment, name='add_comment'),  # Add comment
    path('comment/<int:pk>/edit/', views.update_comment, name='update_comment'),  # Edit comment
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),  # Delete comment
]
