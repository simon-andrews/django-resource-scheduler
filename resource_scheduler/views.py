from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Resource

def index(request):
    return render_to_response("index.html")

def allresources(request):
	mdict = {
		"resources": Resource.objects.all()
	}
	return render_to_response("resources_main.html", mdict)

def specificresource(request, resource_pk):
	mdict = {
		"resource": Resource.objects.get(pk=resource_pk)
	}
	return render_to_response("resource.html", mdict)
