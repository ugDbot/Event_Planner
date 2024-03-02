"""
============================INSTALL AND SETUP DJANGO===============================================================
We start by creating a virtual environment since it's pycharm we click ctrl+Alt+S
we locate the name of our project (which you obviously created a new project before creating the virtual environment)
we select python interpreter
we select add new interpreter
we select virtual environment interpreter and fill the fields according to what we want (Whether new or existing)
I recommend making the virtual environment available to all projects/packages if its an existing one
we then apply it

We then click ctrl+Alt+S to ensure the virtual environment has been activated
we navigate to the project name, python interpreter, then we look at available interpreters from the drop down box
The virtual environment is indicated with a "V" next to the python logo of the interpreter name
then we select the desired interpreter to activate it

We then install django by installing it
In the terminal we type: pip install django
it installs it then we can ctrl+Alt+S and navigate to our project and see the installed packages
or we type pip freeze in the terminal to show installed packages

We then create our django project In the terminal we type: "django-admin startproject first_project"  - "first_project"
will be your name choice of the project
We can type "Ls" in our terminal to see things created and if the first step in done right we should see the project
first_project or whatever name you've given yours
We then move into that project directory by typing: cd first_project in our terminal

We type "Ls" in the terminal after moving into our project dir and we can see a manage.py file which is very important
and is what we use to run django things
We then test our server by typing: "python manage.py runserver" in our terminal
We click the link or copy it into a browser and we should see that we have successfully created our website
!!!WE CLICK Ctrl+C to break out of the whole thing easily!!!
!!!!!!TO RUN THE SERVER WE ALWAYS USE: "python manage.py runserver" in our terminal!!!!!!












==============================ADD APPS TO OUR PROJECT AND SETUP WEBSITE, WEBPAGE AND URLS============================================================
*NOTE THAT YOUR PROJECT PACKAGE FOLDER IS DIFFERENT FROM YOUR APP PACKAGE FOLDER ENDEAVOUR TO NAME THE PROJECT FOLDER WITH "_project" AT THE ENDING OF THE NAME
FOR BETTER UNDERSTANDING AND CLEAN NAMING E.G new_project, django_web_project*

We open our terminal and type: python manage.py startapp "name choice of the app" e.g:
python manage.py startapp events.

Once we do that we add it to the settings, we navigate to our project package folder on pycharm
then we click the drop down and find settings.py and open it
then we navigate to INSTALLED_APPS in the code and add our newly created app to the list (ensure to follow the format
of the list and add your comma at the end just like in the format)

Now to set up url we navigate to our projects package folder and click urls.py
we find the imports (you'll see it as "imports..." just click it to see imports) or it'll be already written out:
it'll be written like this: from django.contrib import admin
                            from django.urls import path
---------------------------------------------------------------------------
now we modify it and add "include": from django.contrib import admin
                                    from django.urls import path, include
---------------------------------------------------------------------------
then we add the path to the urlpatterns which originally look like this:
urlpatterns = [
    path('admin/', admin.site.urls),
]
---------------------------------------------------------------------------
then we modify it and add a new path with the name of our choice app name:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls'))
]
---------------------------------------------------------------------------
Now that we've done that we open the app package folder and create a new urls.py file for our app folder
then we type in:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
]
*the "." in the second import means the current directory where the urls.py file exists (which is our app's folder)
-----------------------------------------------------------------------------
Once we do that, we go to the views.py file in the app's folder and create the function "home":
def home(request):
    return render(request, 'home.html', {})
------------------------------------------------------------------------------
============================TEMPLATES=========================================
We create the "home.html" in our templates dir, if the templates dir hasn't been created:
We go to our app's folder and create new dir and name it "templates"
Then we create a new folder in the template and name it according to the app we want
This is because over time you might have alot of apps so instead of creating new templates
we just create new folders with the name of the app currently being worked on and create our home.html in that folder instead
"home.html" (which is a file not a .py)
And in that file we create a hi tag:
<hi>Hello World!</hi> --- as an intro text
We save all
------------------------------------------------------------------------------
Then we test to see if all us was done properly and test the server i.e "python manage.py runserver"
Which should display "Hello World
------------------------------------------------------------------------------
=========================BASE TEMPLATES===========================
This is a html file which contains the looks and design of our webpage
it'll be created in the templates/app/ folder as base.html





MOST OF OUR WORK WILL BE DONE IN THE VIEWS.PY IN THE APP'S FOLDER WHERE WE CREATED OUR WEBPAGE WITH THE HOME FUNCTION AND ALSO DONE IN THE HOME.HTML FILE
SO FOR MOVING TUTORIALS TO IT, MOST DOCUMENTATION WILL BE IN THOSE FILES






"""