from django.db import models
import json

class GuestbookEntryForm(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50, blank=True)
	comment = models.CharField(max_length=500)
	def toDict(self):
		entry = {"name": self.name, "email": self.email, "comment": self.comment}
		return entry
