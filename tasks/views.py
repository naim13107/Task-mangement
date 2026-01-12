from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q , Count , Max , Min , Avg

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
    #Show the task that are completed
    # tasks = Task.objects.filter(status = "COMPLETED")

    #Show the task whose due date is today
    # tasks = Task.objects.filter(due_date = date.today())

    """"Show the task whose priority is not low """

    # tasks = TaskDetail.objects.exclude(priority = "H")

    '''Show the task that contain letter 'c' and status pending'''
    #tasks = Task.objects.filter(title__icontains  = 'c' , status = 'PENDING')
    
    '''Show the tasks those are in-progress or status pending'''
    #tasks = Task.objects.filter(Q(status = 'PENDING')| Q(status = 'IN_PROGRESS'))
  
    '''to check if any entry exists or not'''
    # tasks = Task.objects.filter(status='kjjsdasdwqwdqwd').exists() 

    #select_related(ForeignKey,OneToOneField)
    # tasks = Task.objects.select_related('details').all
    # tasks = TaskDetail.objects.select_related('task').all
    # tasks = Task.objects.select_related('project').all()

    ''''prefetch_related (reverse Foreignkey , many to many) '''
    #tasks = Project.objects.prefetch_related('task_set').all()

    # tasks = Task.objects.prefetch_related('assigned_to').all()

    # task_count = Task.objects.aggregate(num_task  = Count('id'))

    projects = Project.objects.annotate(num_task = Count('task')).order_by('num_task')
    
    return render(request,"show_task.html",{"projects" : projects })



#Aggrigate SQL - min max .....