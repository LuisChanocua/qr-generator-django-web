from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string

def default_slug():
    return get_random_string(8).lower()

class QRCode(models.Model):
    slug = models.SlugField(primary_key=True, max_length=32, default=default_slug, unique=True)
    title = models.CharField(max_length=120, blank=True)
    target_url = models.URLField(help_text="Destino actual del QR")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.slug} -> {self.target_url}"

class ClickEvent(models.Model):
    qr = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name="clicks")
    ts = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    ua = models.TextField(blank=True, default="")
    ref = models.TextField(blank=True, default="")
