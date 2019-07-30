from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthView.as_view()),
    path('', views.AccountView.as_view())
]