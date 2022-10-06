from django.contrib import admin
from .models import Task


#la siguiente clase nos permite visualizar la fecha de creacion en el panel
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('create', )

# Register your models here.
admin.site.register(Task, TaskAdmin)