from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to myapp page</h1>")
def home(request):
    return render(request,"myapp/home.html",{'name':"reyaz"})
def fact(request,n):
    n=int(n)
    return HttpResponse("<h2>factorial is {}</h2>".format(factorial(n)))