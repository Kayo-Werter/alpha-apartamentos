from django.contrib import admin
from django.conf import settings
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Api da Alpha Apartamentos",
        default_version="v1",
        description="Uma API de gerenciamento de apartamentos para imóveis",
        contact=openapi.Contact(email="kayo.werter2@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema=redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]


admin.site.site_header="Apartamentos Alpha admin"
admin.site.site_title="Apartamentos Alpha portal do admin"
admin.site.index_title="Bem vindo ao portal do admin da Alpha Apartamentos"

