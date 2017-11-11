from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):
	return HttpResponse("This is an App")