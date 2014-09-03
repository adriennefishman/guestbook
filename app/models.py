from django.db import models

class Guestbook(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50, blank=True)
	comment = models.CharField(max_length=500)