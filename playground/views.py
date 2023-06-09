from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 'views' is misleading as a name, it is a request handler
# request -> response

def say_hello(request):
    return render(request, "hello.html", {"name": "Ritz"})
