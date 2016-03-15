from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Houra, princesse arrive enfin à faire quelque chose!")
