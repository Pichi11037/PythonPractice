from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse('Hello World!')

def bye(request):
    return HttpResponse('Bye, see you later... ')

def contact(request):
    return HttpResponse('Name: Andres Pichimata \nTel.: 3213472115 \nEmail: afpichimata@hotmail.com')