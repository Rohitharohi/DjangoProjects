from django.shortcuts import render,HttpResponse

# Create your views here.

def add_courses(request):
    return HttpResponse("<h1>add_course</h1>")

def add_batches(request):
    return HttpResponse("<h1>add_course</h1>")

def add_faculty(request):
    return HttpResponse("<h1>add_faculty</h1>")

def view_timesheets(request):
    return HttpResponse("<h1>timesheets</h1>")
