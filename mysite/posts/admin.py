from django.contrib import admin
from posts.models import Post  #importing Post class from posts app
#When logging into admin site, admin should now be able to create posts
# Register your models here.

admin.site.register(Post)
