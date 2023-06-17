from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    return render(request,'index.html')
def qual(request):
    return render(request,'qual.html')
def extra(request):
    return render(request,'extra.html')
def skills(request):
    return render(request,'skills.html')
def contact(request):
    return render(request,'contact.html')
def personal(request):
    return render(request,'personal.html') 
