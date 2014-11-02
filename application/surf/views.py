from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from surf.models import *

def home(request):
	if request.user.is_authenticated():
		galleries = None
		artists = None#Artist.objects.all()
		return render(request,'home.html',{"data":{"gallery":galleries,"artist":artists}})
	else:
		return redirect('/login')
