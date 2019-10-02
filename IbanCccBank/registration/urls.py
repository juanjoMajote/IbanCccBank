from django.urls import path, include
from . import views

registration_urlpatterns = ([
    path('', views.login, name="login"),
],"registration")