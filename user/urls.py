from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.signin, name="signin"),
    path("register/", views.signup),
    path("logout/", views.signout),
    path("user_page/", views.user_page),
    path("change_password/", views.change_password),
    path("login_post/", views.signin_post, name="signin"),
    ]