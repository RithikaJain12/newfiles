from django.shortcuts import render
from django.http import HttpResponse

def coding(request):
	return render(request,"index.html")
	return HttpResponse("webdeveloper in training")
# Create your views here.
