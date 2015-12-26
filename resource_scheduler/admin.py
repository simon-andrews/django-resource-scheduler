from django.contrib import admin
from .models import Resource, Reservation

class ResourceAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'comment',
	)

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

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Reservation, ReservationAdmin)
