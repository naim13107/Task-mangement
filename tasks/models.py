from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)    

    def __str__(self):
        return self.name     

class Project(models.Model):
    name = models.CharField( max_length=150)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name

class Task(models.Model) :
    STATUS_CHOICES =[
        ('PENDING','pending'),
        ('IN_PROGRESS' , 'In Progress'),
        ('COMPLETED' , 'Completed')
    ]
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,      #many to one
        default=1
        ) # jodi project niche thakto tahole " " qutaion er majhe likte hoito project
    assigned_to = models.ManyToManyField(Employee , related_name='tasks')   
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default="PENDING")
    is_completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title

#One to One 
#Many to one
#many to many

class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
    
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name = 'details'
        )
    
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField( max_length=1 , choices=PRIORITY_OPTIONS , default=LOW)
    notes = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f'Details from Task {self.task.title}'

# Task.objects.get(id=2)
#select * from task where id = 2
# ORM = Object relational Mapper  

#many to many 

#task = many employee 1 task 
# employee = many tasks 1 employee 

