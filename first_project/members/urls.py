from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),

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