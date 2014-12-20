from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'posts.views.index', name='index'),
    url(r'^posts/', include('posts.urls')),
    #routed to posts.urls to show the app, in the case 'posts' content
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
    'django.views.static',(r'media/(?P<path>.*)', 'serve',
    {'document_root':settings.MEDIA_ROOT}),
    )
