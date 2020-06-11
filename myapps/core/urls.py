from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.insertemp, name='save_emp_data'),
    path('api/empnew/', views.saveemp, name='save_api_emp_data'),
]
