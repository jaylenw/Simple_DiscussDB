from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
"""
A model is source of information of th data.  Each model is
a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.


"""
#below defining model the defines Post
class Post(models.Model):

  #Posts will have a title
  title = models.CharField(max_length=80) #title length 80 characters

  #Posts will have a body with text
  body = models.TextField() #content will be inserted here

  #Posts will have datetimefield when content is published automatically
  #time_created = models.DateTimeField(auto_now_add=True)

  #Posts will have user submit datetimefield when making post
  pub_date = models.DateTimeField('date published')

  #Posts will have author field
  author = models.CharField(max_length=30)

  #Posts will have quick summary field
  synopsis = models.TextField()

  #Adding image field for admins to upload picture to post
  image = models.ImageField("Post Image", upload_to="MEDIA_PATH/", blank=True, null=True)


  tag = models.CharField(max_length=30) #Posts will have a tag
  def __unicode__(self):
    return self.title
    #read documentation on why we use the above method in Python 2
