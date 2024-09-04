Lecture 3 - Django.

To install Django: pip3 install Django
To create a new project: django-admin startproject PROJECT_NAME

manage.py is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often. Example: python3 manage.py SUBCOMMAND

settings.py contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.

urls.py contains directions for where users should be routed after navigating to a certain URL.

Start the project by running python manage.py runserver.

Apart:
    Available subcommands:

        [auth]
            changepassword
            createsuperuser

        [contenttypes]
            remove_stale_contenttypes

        [django]
            check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            optimizemigration
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp
            startproject
            test
            testserver

        [sessions]
            clearsessions

        [staticfiles]
            collectstatic
            findstatic
            runserver

Next, we’ll have to create an application. Django projects are split into one or more applications. Most of our projects will only require one application, but larger sites can make use of this ability to split a site into multiple apps. To create an application, we run python manage.py startapp APP_NAME. This will create some additional directories and files that will be useful shortly, including views.py.

Now, we have to install our new app. To do this, we go to settings.py, scroll down to the list of INSTALLED_APPS, and add the name of our new application to this list.

Routes:

Now, in order to get started with our application:

    Next, we’ll navigate to views.py. This file will contain a number of different views, and we can think of a view for now as one page the user might like to see. To create our first view, we’ll write a function that takes in a request. For now, we’ll simply return an HttpResponse (A very simple response that includes a response code of 200 and a string of text that can be displayed in a web browser) of “Hello, World”. 

    Now, we need to somehow associate this view we have just created with a specific URL. To do this, we’ll create another file called urls.py in the same directory as views.py. We already have a urls.py file for the whole project, but it is best to have a separate one for each individual app.

    Inside our new urls.py, we’ll create a list of url patterns that a user might visit while using our website. In order to do this:
        We have to make some imports: from django.urls import path will give us the ability to reroute URLSs, and from . import views will import any functions we’ve created in views.py.

        Create a list called urlpatterns.

        For each desired URL, add an item to the urlpatterns list that contains a call to the path function with two or three arguments: A string representing the URL path, a function from views.py that we wish to call when that URL is visited, and (optionally) a name for that path, in the format name="something".

        Now, we’ve created a urls.py for this specific application, and it’s time to edit the urls.py created for us for the entire project. When you open this file, you should see that there’s already a path called admin which we’ll go over in later lectures. We want to add another path for our new app, so we’ll add an item to the urlpatterns list. This follows the same pattern as our earlier paths, except instead of adding a function from views.py as our second argument, we want to be able to include all of the paths from the urls.py file within our application. To do this, we write: include("APP_NAME.urls"), where include is a function we gain access to by also importing include from django.urls.

        By doing this, we’ve specified that when a user visits our site, and then in the search bar adds /hello to the URL, they’ll be redirected to the paths inside of our new application.

Now that we’ve had some success, let’s go over what just happened to get us to that point:
1. When we accessed the URL localhost:8000/hello/ , Django looked at what came after the
base URL ( localhost:8000/ ) and went to our project’s urls.py file and searched for a
pattern that matched hello .
2. It found that extension because we defined it, and saw that when met with that extension, it
should include our urls.py file from within our application.
3. Then, Django ignored the parts of the URL it has already used in rerouting
( localhost:8000/hello/ , or all of it) and looked inside our other urls.py file for a pattern
that matches the remaining part of the URL.
4. It found that our only path so far ( "" ) matched what was left of the URL, and so it directed
us to the function from views.py associated with that path.
5. Finally, Django ran that function within views.py , and returned the result
( HttpResponse("Hello, world!") ) to our web browser.

In thinking about how this is implemented, it seems impossible that sites like GitHub and Twitter
would have an individual URL path for each of its users, so let’s look into how we could make a
path that’s a bit more flexible. We’ll start by adding a more general function, called greet , to
views.py


Templates

So far, our HTTP Responses, have been only text, but we can include any HTML elements we want
to! For example, I could decide to return a blue header instead of just the text in our index
function.

This is why we’ll now introduce Django’s templates
(https://docs.djangoproject.com/en/4.0/topics/templates/), which will allow us to write HTML and
CSS in separate files and render those files using Django.

In addition to writing some static HTML pages, we can also use Django’s templating language
(https://docs.djangoproject.com/en/4.0/ref/templates/language/) to change the content of our
HTML files based on the URL visited.

You’ll noticed that we used some new syntax: double curly brackets. This syntax allows us to access
variables that we’ve provided in the context argument.

Conditionals:

{% any kinf of logic of Django inside an html file%}
To create another app in the same project, it is the same way as before from startapp onwards.

Styling:

If we want to add a CSS file, which is a static file because it doesn’t change, we’ll first create a
folder called static , then create a newyear folder within that, and then a styles.css file within
that.
Then we have to load the folder and link the styles file with django syntax.

New project steps: (resume)

    1. run python manage.py startapp tasks in the terminal.
    2. Edit settings.py , adding “tasks” as one of our INSTALLED_APPS.
    3. Edit our project’s urls.py file, and include a path similar to the one we created for the
    hello app:
    path('tasks/', include("tasks.urls"))
    4. Create another urls.py file within our new app’s directory, and update it to include a path
    similar to the index path in hello :
    from django.urls import path
    from . import views
    urlpatterns = [
    path("", views.index, name="index"),
    ]
    5. Create an index function in views.py .


Templates inheritance:
All the html files will inherit from a layout html file using django syntax.


Forms:

We need to add a bit more to this form now, because Django requires a token to prevent Cross-Site
Request Forgery (CSRF) Attack (https://portswigger.net/web-security/csrf). This is an attack where a
malicious user attempts to send a request to your server from somewhere other than your site. This
could be a really big problem for some websites. Say, for example, that a banking website has a
form for one user to transfer money to another one. It would be catastrophic if someone could
submit a transfer from outside of the bank’s website!
To solve this problem, when Django sends a response rendering a template, it also provides a CSRF
token that is unique with each new session on the site. Then, when a request is submitted, Django
checks to make sure the CSRF token associated with the request matches one that it has recently
provided. Therefore, if a malicious user on another site attempted to submit a request, they would
be blocked due to an invalid CSRF token. This CSRF validation is built into the Django Middleware
(https://docs.djangoproject.com/en/4.0/topics/http/middleware/) framework, which can intervene
in the request-response processing of a Django app. We won’t go into any more detail about
Middleware in this course, but do look at the documentation
(https://docs.djangoproject.com/en/4.0/topics/http/middleware/) if interested!


Django Forms:

While we can create forms by writing raw HTML as we’ve just done, Django provides an even easier
way to collect information from a user: Django Forms
(https://docs.djangoproject.com/en/4.0/ref/forms/api/).


Sessions:

Sessions are a way to store unique data on the server side for each new visit to a website.
In order to solve this problem we’re going to employ a tool known as sessions. (https://docs.djangoproject.com/en/4.0/topics/http/sessions/).
