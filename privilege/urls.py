from django.conf.urls import patterns, url

urlpatterns = patterns('privilege.views',
    url(r'^$', 'index', name='index'),
    url(r'^sheet/$', 'sheet', name='sheet'),
)
