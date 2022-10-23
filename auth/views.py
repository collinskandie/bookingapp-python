from django.http import HttpResponse
from django.shortcuts import renderang
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello I am home')