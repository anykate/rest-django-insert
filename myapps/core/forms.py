from django import forms
from .models import EmployeeModel


class EmployeeDetailsInsertForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
