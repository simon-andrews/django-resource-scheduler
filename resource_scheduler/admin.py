from django.contrib import admin
from .models import Resource, Reservation

class ReservationAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'resource',
		'priority',
		'reservation_start',
		'reservation_end',
		'due_date',
		'message',
	)

admin.site.register(Resource)
admin.site.register(Reservation, ReservationAdmin)
