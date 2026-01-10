from django import forms 
from tasks.models import Task
#django form 
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250,label='Task Title')
    description = forms.CharField(widget=forms.Textarea,label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget,label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[])

    
    def __init__(self, *args, **kwargs):
        
        employees = kwargs.pop("employees",[])
        #print(args,kwargs)
        super().__init__(*args,**kwargs)
        self.fields['assigned_to'].choices = [
            (emp.id,emp.name) for emp in employees]

class StyledFromMixin :
    """ Mixing to apply style to form field """

    default_classes =" p-3 border-2 border-gray-300 shadow-sm w-full rounded-lg ",

    def apply_styled_widgets(self) :
        for field_name , field in self.fields.items():
            if isinstance(field.widget , forms.TextInput):
                field.widget.attrs.update({
                    'class' : self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}",
                }) 
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class' : f'{self.default_classes} resize-none',
                    'placeholder' : f"Enter {field.label.lower()}",
                    'rows' : 5,
                })    
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class' : "mb-5 border-2 border-gray-100 shadow-sm  rounded-lg",
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class' : "space-y-2",        
                })
            else : 
                field.widget.attrs.update({
                    'class':self.default_classes
                })


#django model form 

class TaskModelForm(StyledFromMixin,forms.ModelForm):
    class Meta : 
        model = Task 
        fields = ['title','description','due_date','assigned_to']
        widgets = { 
            'due_date' : forms.SelectDateWidget,
            'assigned_to' : forms.CheckboxSelectMultiple,
        }
        
        # exclude = ['project','is_completed','created_at','updated_at']
        """Manual widgets"""
        # widgets = { 
        #     'title' : forms.TextInput(attrs={
        #         'class' : " p-3 border-2 border-gray-300 shadow-sm w-full rounded-lg ",
        #         'placeholder' : "Enter Task Title"
        #     }),
        #     'description' : forms.Textarea(attrs={
        #       'class' : "mb-5 border-2 border-gray-100 shadow-sm w-full rounded-lg " ,
        #       'placeholder' : "Enter Task Description",
        #       'rows': 5,
        #     }),
        #     'due_date': forms.SelectDateWidget(attrs={
        #         'class' : "mb-5 border-2 border-gray-100 shadow-sm  rounded-lg " ,
                
        #     }) ,
        #     'assigned_to' : forms.CheckboxSelectMultiple(attrs={
        #         'class' : "space-y-2" ,
                
        #     }),
        # }

    """Üsing mixing widgets"""   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
    