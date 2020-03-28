from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contacts(request):
    return render(request, 'contacts.html')
def course_ad(request):
    return render(request, 'adult.html')
def stud(request):
    return render(request, 'stud.html')