from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_GET
from .models import QRCode, ClickEvent
from .utils import generate_qr_png

@require_GET
def qr_png(request, slug):
    qr = get_object_or_404(QRCode, pk=slug, is_active=True)
    if qr.expires_at and qr.expires_at <= timezone.now():
        return HttpResponseNotFound(b"QR expirado")
    url = request.build_absolute_uri(f"/r/{qr.slug}")
    png = generate_qr_png(url)
    return HttpResponse(png, content_type="image/png")

@require_GET
def qr_redirect(request, slug):
    qr = get_object_or_404(QRCode, pk=slug, is_active=True)
    if qr.expires_at and qr.expires_at <= timezone.now():
        return HttpResponseNotFound(b"QR expirado")
    try:
        ClickEvent.objects.create(
            qr=qr,
            ip=request.META.get("REMOTE_ADDR"),
            ua=request.META.get("HTTP_USER_AGENT","")[:500],
            ref=request.META.get("HTTP_REFERER","")[:500],
        )
    except Exception:
        pass
    return HttpResponseRedirect(qr.target_url)
