from django.shortcuts import render, redirect
from .models import Entry, Style
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from entries.forms import EntryForm
from django.urls import reverse

def index(request):
    entries = Entry.objects.all()
    form = EntryForm()

    if request.POST:
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid:
            entry_form.save()

            
    # if entry.view_count is None:
    #     entry.view_count = 1
    # else:
    #     entry.view_count = entry.view_count +1
    # entry.save()

    context = {'entries': entries, 'form': form}


    return render(request, 'entries/index.html', context)

def post_page(request, slug):
    entry = Entry.objects.get(slug = slug)
    form = EntryForm()

    if request.POST:
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid:
            return HttpResponseRedirect(reverse('post_page', kwargs = {'slug': slug}))
        else:
            return HttpResponseRedirect(reverse('post_page', kwargs = {'slug': slug}))
    if entry.view_count is None:
        entry.view_count = 1
    else:
        entry.view_count = entry.view_count +1

    entry.save()

    context = {'entry': entry, 'form': form}

    return render(request, 'entries/post.html', context)






def detail(request, entry_id):
    return HttpResponse('Looking at entry %s.' % entry_id)

def ratings(request, entry_id):
    # results == ratings
    response = 'Looking at the ratings'
    return HttpResponse(response % entry_id)




