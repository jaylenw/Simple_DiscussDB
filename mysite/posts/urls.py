from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    #ex: /posts/
    url(r'^$', views.index, name='index'),
    #ex: /posts/5/
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    #the above url is using regex expressions talking to
    #def details in views.py
)
