from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plan2fab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('dokumentor.urls', namespace="projects")),
    url(r'^dokumentor/', include('dokumentor.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
)
