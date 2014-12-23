from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'', include('dokumentor.urls', namespace="projects")),
    url(r'^dokumentor/', include('dokumentor.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
)
