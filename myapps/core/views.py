from django.shortcuts import render, redirect
from django.views import View
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from .forms import EmployeeDetailsInsertForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


# Create your views here.
@api_view(['POST'])
def saveemp(request):
    if request.method == 'POST':
        emp_serialized_obj = EmployeeSerializer(data=request.data)
        if emp_serialized_obj.is_valid():
            emp_serialized_obj.save()
            return Response(emp_serialized_obj.data, status=status.HTTP_201_CREATED)
        return Response(emp_serialized_obj.data, status=status.HTTP_400_BAD_REQUEST)


def insertemp(request):
    form = EmployeeDetailsInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            headers = {'Content-type': 'application/json'}
            post_data = requests.post(
                'http://localhost:8000/api/empnew/',
                json=form.cleaned_data,
                headers=headers
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
