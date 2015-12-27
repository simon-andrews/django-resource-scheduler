from django.http import Http404
from django.shortcuts import redirect, render, render_to_response
from .forms import ResourceForm, ReservationForm
from .models import Resource, Reservation

def index(request):
    return render_to_response("index.html")

def allresources(request):
	mdict = {
		"resources": Resource.objects.all()
	}
	return render_to_response("resources_main.html", mdict)

def specificresource(request, resource_pk):
	try:
		mdict = {
			"resource": Resource.objects.get(pk=resource_pk)
		}
	except Resource.DoesNotExist:
		raise Http404("No resources with that primary key were found.")
	return render_to_response("resource.html", mdict)

def newresource(request):
	if request.method == 'POST':
		form = ResourceForm(request.POST)
		if form.is_valid():
			r = Resource(name=request.POST['name'], comment=request.POST['comment'])
			r.save()
			return redirect(allresources)
	else:
		form = ResourceForm()
	return render(request, 'newresource.html', {'form': form})

def allreservations(request):
	mdict = {
		"reservations": Reservation.objects.all()
	}
	return render_to_response("reservations_main.html", mdict)

def specificreservation(request, reservation_pk):
	try:
		mdict = {
			"reservation": Resource.objects.get(pk=reservation_pk)
		}
	except Resource.DoesNotExist:
		raise Http404("No reservations with that primary key were found.")
	return render_to_response("reservation.html", mdict)

def newreservation(request):
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			r = Reservation()
			r.user = request.user
			r.resource = Resource.objects.get(pk=int(request.POST['resource']))
			r.priority = request.POST['priority']
			r.reservation_start = request.POST['reservation_start']
			r.reservation_end = request.POST['reservation_end']
			r.due_date = request.POST['due_date']
			r.message = request.POST['message']
			r.save()
			return redirect(allreservations)
	else:
		form = ReservationForm()
	return render(request, 'newreservation.html', {'form': form})
