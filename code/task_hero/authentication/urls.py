from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "authentication"

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign_up"),
    path('log-in/', LoginView.as_view(template_name="authentication/log-in.html"), name="login"),
    path('log-out/', LogoutView.as_view(), name="logout"),
]