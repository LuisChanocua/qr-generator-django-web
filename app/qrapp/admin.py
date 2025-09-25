from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import QRCode, ClickEvent

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ("slug","title","target_url","is_active","created_at","updated_at","expires_at")
    search_fields = ("slug","title","target_url")
    list_filter = ("is_active",)

@admin.register(ClickEvent)
class ClickEventAdmin(admin.ModelAdmin):
    list_display = ("qr","ts","ip")
    search_fields = ("qr__slug","ip","ua","ref")
    list_filter = ("ts",)
