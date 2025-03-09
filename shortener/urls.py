from django.urls import path
from .views import home, redirect_url, signup_view, login_view, logout_view, analytics_view

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("analytics/", analytics_view, name="analytics"),
    path("<str:short_code>/", redirect_url, name="redirect_url"),
]
