from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task


# Create your views here.
# def home(request) :
#       # work with data-base 
#       # transform data
#       # data pass 
#       # HTTP response / Json response 
#     return HttpResponse("Welcome tho the task management system")

# def contact(request):
#     return HttpResponse("<h1 style = 'color : red '>This is contact page</h1>")

# def show_task(request) :
#     return HttpResponse("<h1>This is our task page</h1>")
# def show_specific_task(request,id):
#     print("id : ",id)
#     print("id type : ", type(id) )
#     return HttpResponse(f"<h1> This is specific task page {id} </h1>")

# def dashboard(request,id):
#     return HttpResponse ("This is Dashboard")


# def show_admin(request):
#     return HttpResponse("This is admin")

def manager_dashboard(request):
    return render(request,"dashboard/manager_dashboard.html")
def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")
def test(request):
    context = {
        "names" : ["Mahmud","Ahmed","Jhon","Mr.X"],
         "age" : 23,
            
    }
    return render(request,"test.html",context)

def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() #FOR GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
   
        if form.is_valid():
         
            form.save()
            return  render(request,'task_form.html',{"form":form , "message" :"Task added successfully"})

    context = {"form" : form}
    return render(request,"task_form.html",context)

def view_task(request):
    #retrive all data from tasks model
    tasks = Task.objects.all()

    #retrive a specific task 
    task_3 = Task.objects.get(pk=3)

    #Fetch the first task 
    first_task = Task.objects.first
    return render(request,"show_task.html",{"tasks" : tasks ,"task3" : task_3 , "first_task":first_task})
