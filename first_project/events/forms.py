"""
Self created .py file to handle our forms logic
We will render it to the screen in views.py

There are different syntax for forms provided to us by django which you can check on their website or online
The one we made use of here are:
TextInput: For an entry format
Select: For a drop down format
SelectMultiple: For multiple selection format
Textarea: For a text field format

The syntax for those are: forms."desired format"(attrs={})
E.g: forms.TextInput(attrs={})

The attrs are also provided to us by django which can researched online or their website

"""

from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# Create a add venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')

        # Customize labels or completely remove them
        labels = {'name': '',
                  'address': '',
                  'zip_code': '',
                  'phone': '',
                  'web': '',
                  'email_address': ''}

        # Customize text field widgets with bootstrap
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
                   'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
                   'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
                   'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
                   'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), }

# Create a add event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')

        # Customize labels or completely remove them
        labels = {'name': '',
                  '': '',
                  'venue': 'Venue',
                  'manager': 'Manager',
                  'attendees': 'Attendees',
                  'description': ''}

        # Customize text field widgets with bootstrap
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                   'event_date': forms.SelectDateWidget(attrs={'class': 'form-select', 'placeholder': 'Date of Event'}),
                   'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
                   'manager': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': "Please put your username in this field"}),
                   'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),}

