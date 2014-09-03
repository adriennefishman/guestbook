from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from guestbook.models import GuestbookEntryForm
import json

def index(request):
    entries = [x.toDict() for x in GuestbookEntryForm.objects.all()]
    return render_to_response('index.html', {"entries": entries},
    context_instance=RequestContext(request))

def update(request):
    form = GuestbookEntryForm()
    form.name = request.POST.get("name_field")
    form.email = request.POST.get("email_field")
    form.comment = request.POST.get("comment_field")
    form.save()
    return HttpResponse(json.dumps(form.toDict()), content_type="application/json")