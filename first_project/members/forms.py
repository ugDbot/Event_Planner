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


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# This adds more fields to django's generated registration(UserCreationForm) form which was used on members/views.py
# And the widgets is put there to customize it
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # A function to customize django's generated registration(UserCreationForm) to make it look better
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
