from django.conf.urls import patterns, url

urlpatterns = patterns('privilege.views',
    url(r'^$', 'index', name='index'),
)
