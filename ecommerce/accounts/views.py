from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def accounts_home(request):
    """Redirige vers le profil si connecté, sinon vers signup"""
    if request.user.is_authenticated:
        return redirect("profile")
    return redirect("signup")

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "registration/profile.html")