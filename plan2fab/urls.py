from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'', include('dokumentor.urls', namespace="projects")),
    url(r'^dokumentor/', include('dokumentor.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
