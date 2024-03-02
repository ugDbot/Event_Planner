from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list events"),
    path('add_venue', views.add_venue, name="add-venue"),
    path('list_venues', views.list_venues, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('searched', views.searched, name='search'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('add_event', views.add_event, name="add-event"),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('venue_text', views.venue_text, name='venue-text'),
    path('my_events', views.my_events, name='my-events'),
    path('search_events', views.search_events, name='search-events'),
]

"""
??ADDITION OF NEW PATHS AND URLS??
We add new paths as we keep coding depending on what your doing by just writing this code:
1. The '' contain the string or number that'll be used to search and will be present in the complete url code
2. The name contains the url link name
3. The views."" is the function containing the logic which is created in the views.py

4. The '<>/<>' are called path converters which are:
   int: Numbers
   str: Words
   path: whole urls
   slugs: hyphen and underscores
   UUID: user numbers
   which the names of whatever is converted will be passed into our home or whatever function depending on your work 
   in our views.py 
--------------------

??CREATING CLICKABLE URL PATHS??
We create a path and and called the search url link any name we want, in ths case we called it "show_venue" and we 
passed in an event variable and in this case we called it "<venue_id>", this event will be called and passed in the
show_venue function just as we call and pass in request as seen in the views.py
Now to make the link clickable we use the line of code:
"<a href="#"></a>" the (#) will contain the link information, which is the path we created
and that line of code will be put in your html file


"""