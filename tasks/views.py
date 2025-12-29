from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request) :
      # work with data-base 
      # transform data
      # data pass 
      # HTTP response / Json response 
    return HttpResponse("Welcome tho the task management system")

def contact(request):
    return HttpResponse("<h1 style = 'color : red '>This is contact page</h1>")

def show_task(request) :
    return HttpResponse("<h1>This is our task page</h1>")
def show_specific_task(request,id):
    print("id : ",id)
    print("id type : ", type(id) )
    return HttpResponse(f"<h1> This is specific task page {id} </h1>")

def show_admin(request):
    return HttpResponse("This is admin")