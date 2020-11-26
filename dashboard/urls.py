from django.contrib import admin
from django.urls import path
from .views.dash import Dash

urlpatterns = [
    path('', Dash.as_view(), name = "homepage")
]