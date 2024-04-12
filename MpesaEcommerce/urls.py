from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path as url
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path as url, include


public_apis = [
    # urls for the auth app
    url(r'^api/v1/ecommerce/', include("shopify.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="ecommerce API",
        default_version="version 1",
        description="These are the main APIs for Athens",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # enable the admin interface
    path('developer/docs', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('developer/doc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^admin/', admin.site.urls)
]

urlpatterns += public_apis

admin.site.site_header = "Ecommerce Admin"
admin.site.site_title = "Mpesa Ecommerce Admin"
admin.site.index_title = "Mpesa Ecommerce Admin"
