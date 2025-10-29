from django.urls import path
from .views import register_view, CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_view, name='register'),  # User registration
    path('login/', CustomLoginView.as_view(), name='login'),  # User login
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # User logout (redirects immediately)
    
    # Optional password reset URLs if needed
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
