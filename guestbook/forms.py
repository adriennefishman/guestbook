from django import forms
from guestbook import models

class GuestbookEntryForm(forms.ModelForm):
	"""This is the Form class from the model.

	It has a form field for every model field specified (name, email, comment).
	"""
	class Meta:
		model = models.GuestbookEntryForm