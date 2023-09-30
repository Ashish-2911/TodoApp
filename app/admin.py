# myapp/admin.py
from django.contrib import admin
from app.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task','is_completed','updated']
    search_fields = ['task',]
    

# Register the model with the custom admin class
admin.site.register(Task, TaskAdmin)
