from django.db import models
import json
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.validators import validate_email
from django.utils.html import escape

class GuestbookEntryForm(models.Model):
	"""This is the model for a Guestbook Entry.

	It has a name, an email and a comment as fields of the model.
	Email is allowed to be blank, but name and comment are not.
	"""
	name = models.CharField(max_length=50, blank=False, error_messages={'required':'Name is required.'})
	email = models.EmailField(max_length=50, blank=True)
	comment = models.CharField(max_length=500, blank=False, error_messages={'required':'Comment is required.'})
	def toDict(self):
		"""This is a method that turns a guestbook entry into a dictionary.

		It has keys of name, email and comment, and the input for these fields are the associated values.
		"""
		entry = {"name": self.name, "email": self.email, "comment": self.comment}
		return entry
	def clean(self):
		if self.name is None:
			raiseValidationError("Name field is required")
	def validateEmail( email ):
	    from django.core.validators import validate_email
	    from django.core.exceptions import ValidationError
	    try:
	        validate_email( email )
	        return True
	    except ValidationError:
	        return False
