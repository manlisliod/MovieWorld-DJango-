from django.urls import path
from .views import LoginView,RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login',LoginView,name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('register',RegisterView,name='register')
]