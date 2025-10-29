from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm

# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Custom login view
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

# Custom logout view (redirects immediately)
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")
