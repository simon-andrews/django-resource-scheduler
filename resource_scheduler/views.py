from django.http import Http404
from django.shortcuts import redirect, render, render_to_response
from .forms import ResourceForm
from .models import Resource

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
