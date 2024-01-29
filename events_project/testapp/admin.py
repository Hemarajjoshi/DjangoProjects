from django.contrib import admin
from .models import *

# Register your models here.

class PaticpantAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'prepared_by', 'project_description']


admin.site.register(Viewers)
admin.site.register(Paticipant, PaticpantAdmin)

