from django.db import models
from django.contrib.auth.models import User



"""
We create a class of the table name, pass in the (models.Model) then specify what we want in our table
and django handles the database troubles

For Every Change you make, you make a migration(database)
you then push the migration which is done in the terminal:
"python manage.py makemigrations" ....then we push it with "python manage.py migrate

We import this models in the admin.py file
--------------------
def __str__(self):
    return self."desired variable"
That function above allows us to decide what to be shown when a user is filling a form
if a value is assigned to the desired variable the user can see the values assigned to it and select form it too
if you programmed it that way
"""



class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip code', max_length=10)
    phone = models.CharField('Contact phone', max_length=20, blank=True)
    web = models.URLField('website address', blank=True)
    email_address = models.EmailField(blank=True)
    owner = models.IntegerField("Venue owner", blank=False)

    # this allows us to decide what can be shown
    def __str__(self):
        return self.name


class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    # this allows us to decide what can be shown
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)  # this allows us to connect
    # two or more tables and to
    # create one if it doesn't exists
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True)

    # this allows us to use the table in the admin area
    def __str__(self):
        return self.name

