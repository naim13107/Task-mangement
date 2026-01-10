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
        # form = TaskModelForm(request.POST, employees = employees)
        if form.is_valid():
            ''' For Model Form Data '''
            # print(form)
            form.save()
            return  render(request,'task_form.html',{"form":form , "message" :"Task added successfully"})
            '''For Django From data'''
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')
            
            # task = Task.objects.create(
            #     title=title,
            #     description = description,
            #     due_date = due_date )
            
            # #Assign employee to tasks 

            # for emp_id in assigned_to : 
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assigned_to.add(employee)
            
            # return HttpResponse("Task Added successfully")

    context = {"form" : form}
    return render(request,"task_form.html",context)