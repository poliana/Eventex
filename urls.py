from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.homepage', name='homepage'),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    )