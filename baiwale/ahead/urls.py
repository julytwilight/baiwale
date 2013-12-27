from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ahead.views.home.index', name='home'),
    url(r'^about/$', 'ahead.views.home.about', name='about'),

    url(r'^(?P<menu>fashion)/$', 'ahead.views.home.whale', name='menu'),
    url(r'^(?P<menu>tasty)/$', 'ahead.views.home.whale', name='menu'),
    url(r'^(?P<menu>pretty)/$', 'ahead.views.home.whale', name='menu'),
    url(r'^whale/(?P<id>\d+)/$', 'ahead.views.home.show', name='whale'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )