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
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from .models import Venue
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# This is where we create our webpages functions

def search_events(request):
    # if the user clicked the search button
    if request.method == "POST":

        # get what the user typed which the variable "name" in the search navbar widget is holding
        searching = request.POST["searcher"]

        # filter through venue for the name of a venue, in this case we are only searching through venue
        resultEvent = Event.objects.filter(name__contains=searching)

        return render(request, 'events/search_events.html', {'searched': searching,
                                                          'results2': resultEvent})
    else:
        return render(request, 'events/search_events.html', {})




# My events page
def my_events(request):
    # If the user is logged in
    if request.user.is_authenticated:
        current_user_id = request.user.id
        list_events = Event.objects.filter(attendees= current_user_id)
        return render(request, 'events/myevents.html', {'current_user_id': current_user_id, 'list_events': list_events})


    else:
        messages.success(request, 'Access Denied')
        return redirect('home')


# Generate Text file Venue List (THIS HAS TUTORIAL CODE ON HOW TO ADD A DOWNLOAD OPTION)
def venue_text(request):
    # Define a response to return a text file instead of html
    response = HttpResponse(content_type='text/plain')
    # Create the download function and decide the name of the file/document/exe
    response['Content-Disposition'] = 'attachment; filename=list of venues.txt'
    """
    # Manually add data to the text
    lines = ["This is a test for the notepad\n",
             "This is line 2 with\n",
             "Tester"]
    """
    # Dynamically add data to the text
    all_venues_to_list = Venue.objects.all()
    lines = []
    for venues in all_venues_to_list:
        lines.append(f'{venues}\n')

    response.writelines(lines)
    return response


def delete_venue(request, venue_id):
    # Get venue_id/primary key(pk) that we want to delete
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()

    return redirect('list-venue')


def delete_event(request, event_id):
    # Get event_id/primary key(pk) that we want to delete
    event = Event.objects.get(pk=event_id)
    event.delete()

    return redirect('list events')


def update_event(request, event_id):
    # Get event_id/primary key(pk) that we want to update
    event = Event.objects.get(pk=event_id)

    # Create form for updating which we have created with forms.py, and insert the event the user clicked with instance
    form = EventForm(request.POST or None, instance=event)

    # If the user has updated, we add the redirect module to redirect to a page after updating
    # The redirect is module which we added in here: from django.shortcuts import render, redirect
    if form.is_valid():
        form.save()
        return redirect('list events')

    return render(request, 'events/updateEvent.html', {'updateevent': event, 'form': form})


def add_event(request):
    # Check if the form has been submitted or not
    submitted = False
    manager = Event.objects.all()
    # If the form has been submitted/POST?....
    if request.method == "POST":  # Request.method can be found in the AddEvent.html file
        form = EventForm(request.POST)  # EventForm is the form we created forms.py
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                '/add_event?submitted=True')  # This redirects the user back to the add event page and saves the
            # information
    else:
        form = EventForm
        # if the user submitted and his/her information has been saved?....
        if 'submitted' in request.GET:
            submitted = True

    # Render and show the information like a tkinter Label
    return render(request, 'events/AddEvent.html', {'form': form, 'submitted': submitted, 'manager': manager})


def update_venue(request, venue_id):
    # Get venue_id/primary key(pk) that we want to update
    venue = Venue.objects.get(pk=venue_id)
    venue_user_id = venue.owner  # Get the user who created the venue

    # Create form for updating which we have created with forms.py, and insert the venue the user clicked with instance
    form = VenueForm(request.POST or None, instance=venue)

    # If the user has updated, we add the redirect module to redirect to a page after updating
    # The redirect is module which we added in here: from django.shortcuts import render, redirect
    if form.is_valid():
        form.save()
        return redirect('list-venue')

    return render(request, 'events/updateVenue.html', {'updatevenue': venue, 'form': form,
                                                       'venue_user_id': venue_user_id})


def searched(request):
    # if the user clicked the search button
    if request.method == "POST":

        # get what the user typed which the variable "name" in the search navbar widget is holding
        searching = request.POST["searcher"]

        # filter through venue for the name of a venue, in this case we are only searching through venue
        resultVenue = Venue.objects.filter(name__contains=searching)

        resultEvent = Event.objects.filter(name__contains=searching)

        return render(request, 'events/SearchPage.html', {'searched': searching, 'results1': resultVenue,
                                                          'results2': resultEvent})
    else:
        return render(request, 'events/SearchPage.html', {})


def show_venue(request, venue_id):
    # We passed in venue_id from what we passed in the url.py path for show_venue to help...
    # us search the automatically generated id "pk" (primary key) in django which helps us create a clickable link
    showing_venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=showing_venue.owner)  # Get the venue owner name which is originally in integers
    # from the user model in events/models.py which was imported with the 'from django.contrib.auth.models import User'
    return render(request, 'events/Venue2.html', {'showing_venue': showing_venue, 'venue_owner': venue_owner})


def list_venues(request):
    # grab all the data in the Venue database
    venue_list = Venue.objects.all()
    # Render and show the information like a tkinter Label
    return render(request, 'events/Venue1.html', {'venue_list': venue_list})


def add_venue(request):
    # Check if the form has been submitted or not
    submitted = False
    # If the form has been submitted/POST?....
    if request.method == "POST":  # Request.method can be found in the AddVenue.html file
        form = VenueForm(request.POST)  # VenueForm is the form we created forms.py
        if form.is_valid():  # If the form is filled
            venue = form.save(commit=False)  # Prepare the form for saving
            venue.owner = request.user.id  # Add the user id to the owner slot in the events/models.py
            venue.save()  # Save the form
            return HttpResponseRedirect(
                '/add_venue?submitted=True')  # This redirects the user back to the add venue page and saves the
            # information
    else:
        form = VenueForm
        # if the user submitted and his/her information has been saved?....
        if 'submitted' in request.GET:
            submitted = True

    # Render and show the information like a tkinter Label
    return render(request, 'events/AddVenue.html', {'form': form, 'submitted': submitted})


def all_events(request):
    # grab all the data in the Event database
    event_list = Event.objects.all()
    # Render and show the information like a tkinter Label
    return render(request, 'events/Event_list.html', {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
    # Capitalize month
    month = month.capitalize()

    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create Calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    year_now = now.year

    # Render and show the information like a tkinter Label
    return render(request, 'events/home.html', {
        "first_name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "year_now": year_now,
    })
