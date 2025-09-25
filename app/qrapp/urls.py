from django.urls import path
from . import views

urlpatterns = [
    path("q/<slug:slug>.png", views.qr_png, name="qr_png"),
    path("r/<slug:slug>", views.qr_redirect, name="qr_redirect"),
]
