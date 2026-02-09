from django import template 
from django.utils import timezone
from datetime import datetime 

register = template.Library()

@register.filter
def humanized_date(value):
    if value : 
        today = datetime.now().date()
        value = timezone.localtime(value)
        if value.date() == today :
            return f'Today at {value.strftime("%I:%M %p")}'
        if value.date() == today.replace(day = today.day - 1):
            return f'Yesterday at {value.strftime("%I:%M %p")}'
        else : 
            return f'{value.date().strftime('%B %d')} , {value.strftime("%I:%M %p")}'
        
    return "No login record available"    

