from django.conf.urls import patterns, url

from dokumentor import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'new', views.name_step, name='name_step'),
        url(r'create', views.create, name='create'),
        )

