from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from guestbook.models import GuestbookEntryForm
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    """This is a method that takes a web request and returns the web response of the index.html template.

    It takes each of the form field elements and calls the toDict() method that is written in models.py.
    """
    entries = [x.toDict() for x in GuestbookEntryForm.objects.all()]
    return render_to_response('index.html', {"entries": entries},
    context_instance=RequestContext(request))

def update(request):
    """Once the user fills out the form, this is a method that takes a web request and returns the web response of the index.html template.

    It saves all of the user input fields from the form.
    It then takes the Python dictionary data structure and returns it as a JSON string.
    """
    guestbook_entries = GuestbookEntryForm.objects.all()
    paginator = Paginator(guestbook_entries, 10)
    form = GuestbookEntryForm()
    form.name = request.POST.get("name_field")
    form.email = request.POST.get("email_field")
    form.comment = request.POST.get("comment_field")
    if form.name != None and form.comment != None:
        form.save()
        return HttpResponse(json.dumps(form.toDict()), content_type="application/json")
    else:
        errors = json.dumps(form.errors)
        return HttpResponse(errors, mimetype='application/json')