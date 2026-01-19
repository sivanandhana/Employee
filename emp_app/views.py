from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from emp_app.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

class EmployeeCreateListView(View):

    def get(self,request,*args,**kwargs):

        
