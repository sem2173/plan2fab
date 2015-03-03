from django.conf.urls import patterns, url

from dokumentor import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^projects/(\d+)/$', views.view_project, name='view_project'),
        url(r'name_step', views.name_step, name='name_step'),
        url(r'photo_step/(\d+)/$', views.photo_step, name='photo_step'),
        url(r'build_step', views.build_step, name='build_step'),
        url(r'better_description/(\d+)/$', views.better_description, name='better_description'),
        )
