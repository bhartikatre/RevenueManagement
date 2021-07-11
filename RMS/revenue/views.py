from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def revenue(request,s):
    return HttpResponse(f"Hello this is {s} page")