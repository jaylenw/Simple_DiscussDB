from django.conf.urls import patterns, url
from posts import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    #ex: /posts/
    #ex: /posts/5/
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    #the above url is using regex expressions talking to
    #def detail in views.py
    url(r'^feeder/', views.paginator, name="paginator"),
)
