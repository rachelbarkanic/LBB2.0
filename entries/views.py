from django.shortcuts import render
from .models import Entry, Style
from django.http import HttpResponse, HttpRequest

def index(request):
    entries = Entry.objects.all()
    context = {'entries': entries}

    return render(request, 'entries/index.html', context)


def detail(request, entry_id):
    return HttpResponse('Looking at entry %s.' % entry_id)

def ratings(request, entry_id):
    # results == ratings
    response = 'Looking at the ratings'
    return HttpResponse(response % entry_id)
