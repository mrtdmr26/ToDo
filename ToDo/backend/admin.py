from django.contrib import admin
from .models import Todo 

# Register your models here.

class TodoAdmin(admin.ModelAdmin):  
    list_display = ('uid','title', 'description', 'duedate' , 'completed') 

    
admin.site.register(Todo, TodoAdmin)