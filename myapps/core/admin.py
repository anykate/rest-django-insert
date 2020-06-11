from django.contrib import admin
from .models import EmployeeModel


# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmployeeModel, EmployeeModelAdmin)
admin.site.site_header = 'Haritha Computers & Technology'
