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


def detail(request, post_id):
    try:
      post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
      raise Http404
    return render(request, 'posts/detail.html',{'post':post})
    #look at comments in views.py
    #visitor visits specific post

def listing(request):
    all_posts_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 10) # Show 10 list per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"posts": posts})
