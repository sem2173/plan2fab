from django.conf.urls import patterns, url

from dokumentor import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'name_step', views.name_step, name='name_step'),
        )

