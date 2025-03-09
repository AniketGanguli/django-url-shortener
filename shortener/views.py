from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import ShortenedURL
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

def home(request):
    """Handles URL shortening"""
    short_url = None

    if request.method == "POST":
        original_url = request.POST.get("original_url")
        custom_code = request.POST.get("custom_code", "").strip()

        if not original_url:
            return JsonResponse({"error": "Please enter a valid URL"}, status=400)

        # Generate short code if not provided
        short_code = custom_code or get_random_string(6)

        # Check if the short code is already taken
        if ShortenedURL.objects.filter(short_code=short_code).exists():
            return JsonResponse({"error": "Custom short URL already taken"}, status=400)

        user = request.user if request.user.is_authenticated else None

        # Save to database
        shortened_url = ShortenedURL(original_url=original_url, short_code=short_code, user=user)
        shortened_url.save()

        short_url = request.build_absolute_uri(reverse("redirect_url", args=[shortened_url.short_code]))
        print(f"Shortened URL created: {short_url}")  # Debugging

    return render(request, "shortener/home.html", {"short_url": short_url})
def redirect_url(request, short_code):
    """Redirects a short URL to its original URL."""
    short_url = get_object_or_404(ShortenedURL, short_code=short_code)

    if short_url.is_expired():
        messages.error(request, "This shortened URL has expired.")
        return redirect("home")

    short_url.click_count += 1
    short_url.save()
    return HttpResponseRedirect(short_url.original_url)

def signup_view(request):
    """Handles user signup."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")

    return render(request, "shortener/signup.html", {"user": request.user})

def login_view(request):
    """Handles user login."""
    form = AuthenticationForm()  # ✅ Add form instance

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # ✅ Process form data
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "shortener/login.html", {"form": form})  # ✅ Pass form to template

def logout_view(request):
    """Handles user logout."""
    logout(request)
    return redirect("home")

@login_required
def analytics_view(request):
    """Displays analytics for the logged-in user."""
    user_urls = ShortenedURL.objects.filter(user=request.user)

    if not user_urls.exists():
        messages.info(request, "You have not shortened any URLs yet.")

    return render(request, "shortener/analytics.html", {"user_urls": user_urls, "user": request.user})
