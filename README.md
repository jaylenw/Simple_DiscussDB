Simple Discussion Board/Blog
============================

###Goal:

1.  Have administrators post up topics.  Have visitors post comments with Disqus.  

2.  Content shall be presented aesthetically.

3.  Boom. That's it.  

4.  View video below to see a demo of Simple DiscussDB.

    [Simple DiscussDB Video](http://youtu.be/azxvbZJ1waQ)

5.  Pull Requests & Issues are welcomed.


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

    this created our new site and project.  You should see an 'oursite' directory.

8.  In the repository you downloaded our project site is called mysite, for us it is called
    oursite.  This is the time where you compare, copy, and make additions to the
    files in our 'oursite' directory.  Note: don't replace anything that says oursite
    to our site, just use the repository's code as guide for changes you must make to
    oursite.

9.  Lets now get this site fired up.  We will be creating our database and a
    super user we can use to login to the admin portion of site. cd into 'oursite'
    directory.  You should now see a file that says manage.py.  Run in that directory,

        python manage.py migrate

        python manage.py createsuperuser

10. It is now time to fire up the built in developer server.  Sign into the admin
    site with the superuser you created.  Run,

        python manage.py runserver

11. Go to the browser and enter in the address bar 127.0.0.1:8000/admin
    Login, create a post.  Log out, and visit 127.0.0.18000, thats the home page.

12. You are done. :)

Note: If you ever have to add fields to models.py after creating your database,
run,

        python manage.py makemigrations

        python manage.py migrate


##Running in Production:

1.  Assuming you have done the steps above!

2.  Run,

        sudo pip install gunicorn

    Gunicorn is a Python WSGI HTTP server will be using in replacing Django's
    built in development server.

3.  In settings.py of 'oursite', add the line,

        STATIC_ROOT = os.path.join(PROJECT_PATH,'django_collected_static')

    This line will create a directory of all of our static files we will serve
    with another webserver.

4.  In the same directory where you see manage.py, run

        python manage.py collectstatic

    The directory django_collected_static is now created with our files.


5.  In settings.py now change the following,

        DEBUG = False

        TEMPLATE_DEBUG = False

        ALLOWED_HOSTS = ['127.0.0.1','localhost', '.example.com',]

    Where example.com is the domain you will be using to point to your website.
    .example will catch all subdomains as well.

6.  The following instructions can now be done in multiple ways, but of course this
    is one way.

7.  Make sure django_collected_static folder is in same directory as manage.py.
    Copy admin, bootstrap, and endless_pagination folders from djangoe_collected_static
    into your static folder.


8.  Next, if not already installed, install nginx.  And read the documentation if
    needed to become familiar with it. Because I am cool, I will provide an
    example of an extremely basic configuration file.

        server {


            listen 80;  #listening on port 80
            server_name example.com; #our domain name
            root path; #path to your project, should see static folder
            keepalive_timeout 5;
        #to serve to proxy, gunicorn that is running on port 8000;
            location / {

                proxy_pass http://127.0.0.1:8000;


              }
        #to serve static files

            location /static/  {

              autoindex on;
              alias path/static/; #your path plus addition to static directory

            }

            location /media/ {

              autoindex on;
              alias path/media/;		#your path plus addition to media directory

            }


          }

9.  Make sure you save and restart nginx for configuration to be active.

10. Now back to the directory of our project where manage.py sits, we can now
    launch our project.  Gunicorn runs our project like this,
    gunicorn test_project.wsgi:application ,  for our case, run,

        gunicorn oursite.wsgi:application

    Gunicorn should be running, and now we are all set!

11. If you have your domain name pointing to your server, entering it to the address
    bar should result in your Django site!  Congratulations! :)

12. To make your life easier, and don't want to start you django site manually
    after server reboots, create a bash script.  Lets name it startdjango.sh . In it add,

        #!/bin/bash

        echo "Taking actions to start up Django Site"

        echo "Starting our virtual environment"

        cd pathtositedirectory

        source pathtositedirectory/env/bin/activate

        echo "Ran command to activate virtual environment"

        echo "Changing directories to access our application..."

        cd pathtositedirectory/oursite

        echo "Starting our Django Application"

        gunicorn oursite.wsgi:application  

      Save it.  Then run it by

        source startdjango.sh

13. In an event you need to kill gunicorn, run,

        pkill gunicorn

14. Last but not least!  Your visitors need a way to comment!  Follow Disqus
    instructions on how to add Disqus comments to your site.  You should be able
    to embed code to the file detail.html.
