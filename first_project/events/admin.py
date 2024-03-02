from django.contrib import admin
from .models import Venue
from .models import user
from .models import Event

# Register your models here.

admin.site.register(Venue)
admin.site.register(user)
admin.site.register(Event)
