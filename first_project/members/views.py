# =========================DOCUMENTATIONS AND GUIDES===============================
"""
NOTE: For all tutorials there are functions created by UG referencing or making use of them which serves as examples
And this tutorial is always put at the top of the views.py file for all apps
if you don't find a reference or example in the current views.py file your in? ensure to check all views.py files
for the example your looking for

??RENDERING??
This is like showing the information like a tkinter Label widget
--------------------

??CONTEXT DICTIONARIES??
the "{}" is a context dictionary used to add things from the backend to the frontend of our webpage
We can create variables and pass them into the dictionary to be used in our home.html file
We use "{{}}" in the home.html file to then call this variables e.g *in the home.html file: <hi>Hello {{first_name}}!<h1>
--------------------

??COMMENTING IN OUR HTML FILE??
We use  e.g: "<! hi > to comment, the "<! >" brackets are used so don't get confused if it's in our home.html file
--------------------

??PASSED NAMES AND CONVERTERS??
The "year", "month" names passed into our functions are converters which will take input from the user on our url, this were created in the urls.py file
and passed into the function here. We add datetime.now() to get the system's current dates as events so that if the user doesn't put an input our homepage will still load
and use the datetime.now() function instead
This will be used more often depending on what you want in your program
--------------------

??USING CALENDARS??
we type: "import calendar" and "from calendar import HTMLCalendar"
In our function we convert the month to it's number so we can use it and we also capitalize it to avoid errors
--------------------

??ADDITION OF BOOTSTRAPS/DESIGN??
From the website getbootstrap.com select v5.0 (recommended)
Click introduction and then scroll to started code and copy the code there and paste it in the base.html file
Read the docs to understand it but ensure the bootstrap link is provided and ensure that anything you want to add
into the code is in the body section e.g locate the code <body>
As you keep adding bootstraps for neater code you'll create new htmls containing the designs and you'll call them
in the main html file which is the base.html in this case using the "include" code line i.e {% include "html.file" %}
THE BASE.HTML HOLDS ALL THE DESIGNS
--------------------

??DATABASES??
This is handled in the models.py file which is located in the app's package folder
--------------------

??DJANGO.HTTP import HTTPRESPONSEREDIRECT??
This is used to redirect the page back to itself
--------------------

??CREATING DIFFERENT DOCUMENTS INSTEAD OF ONLY WEBPAGES??
We can create a link and a view that opens texts, Notepad, Pdf and so on with the:
"from django.http import HttpResponse" command
--------------------

??DJANGO AUTHENTICATION??
We use the import code: 'from django.contrib.auth import authenticate, login, logout'
for log in and log out functions
--------------------

??DJANGO REGISTRATION??
We use the import code: 'from django.contrib.auth.forms import UserCreationForm'
to use django's already set registration form and function
--------------------

??MESSAGES POP UPS??
We use the import code: 'from django.contrib import messages'
for pop up messages


"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def login_user(request):
    global user
    # Check if they filled the login form or just visited the page
    if request.method == "POST":  # If the user clicked the login?
        username = request.POST['username']  # Get the username
        password = request.POST['password']  # Get the password
        user = authenticate(request, username=username, password=password)  # Check if they are both correct
        if user is not None:  # If the user exists?
            login(request, user)  # The login is from our imported login
            return redirect('home')  # Redirect to home page.
        else:
            # Return an 'invalid login' error message which is gotten from our import messages
            messages.success(request, ('There was an Error Logging in, Try Again...'))
            return redirect('login')  # Redirect back to login page.

    else:
        return render(request, 'Authentication/Login.html', {})



def logout_user(request):
    logout(request)  # The logout is from our imported login
    messages.success(request, ('Logged out'))  # Return an 'invalid login' error message which is gotten from our
    # import messages
    return redirect('home')  # Redirect to home page.

def register_user(request):
    # Check if they filled the register form or just visited the page
    if request.method == "POST": # If the user clicked sign up
        form = RegisterUserForm(request.POST) # Show the form which was made in members/forms.py
        # and Get the user details
        if form.is_valid(): # once the user filled it all
            form.save() # Save the data
            username = form.cleaned_data['username'] # Get the username
            password = form.cleaned_data['password1'] # Get the confirmed password, cause when signing up..
            # Websites normally ask for first password and confirmation of that password
            user = authenticate(username=username, password=password) # Check if they are both correct
            login(request, user) # Login the user
            messages.success(request, ("Registered Successfully")) # Success message
            return redirect('home') # Take them to homepage
    else: # if the user just visited the page
        form = RegisterUserForm() # show the form and pass it in the render context dictionary to show the page
    return render(request, 'Authentication/register.html', {'form': form})
