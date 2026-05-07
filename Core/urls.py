
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/acounts/', include('apps.accounts.urls')),
    path('api/Profile/', include('apps.Profile.urls')),
    path('api/services/', include('apps.services.urls')),
    path('api/jobs/', include('apps.jobs.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)