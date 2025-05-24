from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

if settings.DEBUG:
    urlpatterns = [
       path('admin/', admin.site.urls),
       path('newa/', include('Newa.urls')),
       path('ckeditor/', include('ckeditor_uploader.urls')),
       path('captcha/', include('captcha.urls')),
    ] + debug_toolbar_urls()

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
