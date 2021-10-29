from django.shortcuts import render,HttpResponse

# Create your views here.
def add_todo(request):
    return HttpResponse("<h1>add_todo</h1>")


def list_todo(request):
    return HttpResponse("<h1>list_todo</h1>")