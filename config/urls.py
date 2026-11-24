from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from accounts.views import StaffLoginView, StaffLogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path("dashboard/login/", StaffLoginView.as_view(next_page="/dashboard/"), name="dashboard-login"),
    path("dashboard/logout/", StaffLogoutView.as_view(), name="dashboard-logout"),
    path("django-admin/login/", RedirectView.as_view(url=reverse_lazy("dashboard-login"), permanent=False)),
    path("django-admin/logout/", RedirectView.as_view(url=reverse_lazy("dashboard-logout"), permanent=False)),
    path("django-admin/", admin.site.urls),
    path("", include("core.urls")),
    path("work/", include("portfolio.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("contact/", include("contact.urls")),
]

# Serve local media only when Cloudinary is not configured (local development fallback).
if not settings.CLOUDINARY_URL:
    from django.urls import re_path
    from django.views.static import serve

    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
