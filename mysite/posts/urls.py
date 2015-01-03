from django.conf.urls import patterns, url
from posts import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    #ex: /posts/
    #ex: /posts/5/
    url(r'^(?P<post_id>\d+)/[\s\S]*', views.detail, name='detail'),

    #so in the url of browser, to acess specific post, root/posts/x/, where
    #x is the number (id) refering to the post
    #[\s\S]* catches everything after root/posts/x/, our post.slug hits this


    #the above url is using regex expressions talking to
    #def detail in views.py
    url(r'^feeder/', views.paginator, name="paginator"),

    #so in the url of browser, access
    #the feed by root/posts/feeder

)
