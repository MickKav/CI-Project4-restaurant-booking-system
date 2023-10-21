from django.contrib import admin
from .models import Booking
from .forms import BookTableForm


admin.site.register(Booking)