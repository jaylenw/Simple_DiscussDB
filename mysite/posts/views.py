from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from posts.models import Post #Post class in models.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    context = {'latest_post_list':latest_post_list}
    return render(request, 'posts/index.html', context)
    #visitor sees five latest posts
    #it is the home page


def detail(request, post_id):
    try:
      post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
      raise Http404
    return render(request, 'posts/detail.html',{'post':post})
    #look at comments in views.py to know how to access page
    #visitor visits specific post
    #specific posts page

def paginator(request):
    paginator_post_list = Post.objects.all().order_by('-pub_date')
    #the feed shall start from latest to oldest from code above
    context = {'paginator_post_list':paginator_post_list}
    return render(request, 'posts/paginator.html', context)
    #look at comments in views.py to know how to access page
    #visitor visits a page with endless lists of posts

def search(request):
    search_query_set = Post.objects.all()
    context = {'search_query_set':search_query_set}
    return render(request,'posts/search.html', context)
