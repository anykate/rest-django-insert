from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    empname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.empname

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
