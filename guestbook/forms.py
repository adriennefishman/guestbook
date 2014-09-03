from django import forms
from guestbook import models

class GuestbookEntryForm(forms.ModelForm):
	class Meta:
		model = models.GuestbookEntryForm