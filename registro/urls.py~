from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.lista'),
    url(r'^adiciona/$', 'core.views.adiciona'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^item/(?P<nr_item>\d+)/$', 'core.views.item'),
    url(r'^remove/(?P<nr_item>\d+)/$', 'core.views.remove'),
)
