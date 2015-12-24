from django.contrib.auth.models import User
from django.db import models

priority_choices = (
	('l', 'Low'),
	('n', 'Normal'),
	('h', 'High'),
	('c', 'Critical')
)

class Resource(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Reservation(models.Model):
	user = models.ForeignKey(User)
	resource = models.ForeignKey(Resource)
	priority = models.CharField(max_length=1, choices=priority_choices)
	reservation_start = models.DateTimeField()
	reservation_end = models.DateTimeField()
	due_date = models.DateTimeField(blank=True, null=True)
	message = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{r} ({u}/{p})".format(r=self.resource,
											u=self.user,
											p=self.priority)
