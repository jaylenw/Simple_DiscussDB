from django.db import models

# Create your models here.
"""
A model is source of information of th data.  Each model is
a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.


"""
#below defining model the defines Posts
class Posts(models.Model):

  #Posts will have a title
  title = models.CharField(max_length=80) #title length 80 characters

  #Posts will have a body with text
  body = models.TextField() #content will be inserted here

  #Posts will have datetimefield when content is published
  time_created = models.DateTimeField(auto_now_add=True)
  def __unicode__(self):
    return self.title
    """ This is python 2. It’s important to add __unicode__() methods
    (or __str__() on Python 3) to your models,not only for your own sanity
    when dealing with the interactive prompt, but also because objects’
    representations are used throughout Django’s automatically-generated
    admin. Python 3 would be different. Info from Django Docs """

  def __unicode__(self):
    return self.title
