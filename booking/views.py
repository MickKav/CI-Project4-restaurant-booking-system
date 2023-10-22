from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import BookTableForm
from booking.models import Booking

def book_table(request):
    if request.method == 'POST':
        form = BookTableForm(request.post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = BookTableForm()
    return render(request, 'book_table.html', {'form': form})