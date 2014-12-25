Simple Discussion Board/Blog
============================

###Goal:

1.  Have administrators post up topics.  Have visitors post comments with Disqus.  

2.  Content shall be presented aesthetically.

3.  Boom. That's it.  


##Running in Test Environment:

Assuming running on GNU/Linux

1.  First download the git repository.  

2.  Globally, need to have python-dev (debian specific) and python-setuptools, python-pip installed.

3.  Creating a directory for our project and then cd into it.

4.  In our new directory, run

        sudo pip install setuptools
        sudo pip install virtualenv
        sudo pip install virtualenvwrapper

        virtualenv env

    you should now see a directory appear named env

5.  Now to activate our virtual environment, run

        source env/bin/activate

6.  Now that we got our virtual environment running we can install
    the software we need.  Copy the requirements.txt file from the
    repository files you downloaded into the same directory and the
    folder env.  Then run,

        pip install -r requirements.txt

7.  Now that our software we need is installed, we must run the following
    command to setup our own django project. Run,

        django-admin startproject oursite

    this created our new site and project.  You should see an oursite directory.

8.  In the repository you downloaded our project site is called mysite, for us it is called
    oursite.  This is the time where you compare, copy, and make additions to the
    files in our oursite directory.  Note: don't replace anything that says oursite
    to our site, just use the repository's code as guide for changes you must make to
    oursite.

9.  Lets now get this site fired up.  We will be creating our database and a
    super user we can use to login to the admin portion of site. cd into oursite
    directory.  You should now see a file that says manage.py.  Run in that directory,

        python manage.py migrate

        python manage.py createsuperuser

10. It is now time to fire up the built in developer server.  Sign into the admin
    site with the superuser you created.  Run,

        python manage.py runserver

11. Go to the browser and enter in the address bar 127.0.0.1:8000/admin
    Login, create a post.  Log out, and visit 127.0.0.18000, thats the home page.

12. You are done.

##Running in Production:
