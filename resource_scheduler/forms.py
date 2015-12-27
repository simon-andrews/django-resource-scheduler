from django import forms
from .models import Reservation, Resource

class ResourceForm(forms.ModelForm):
	class Meta:
		model = Resource
		fields = ['name', 'comment']

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ['resource', 'priority', 'reservation_start', 'reservation_end', 'due_date', 'message']
