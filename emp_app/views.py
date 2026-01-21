from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from emp_app.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCreateListView(View):

    def get(self,request,*args,**kwargs):
         
         qs = Employee.objects.all()

         result =[{"id":emp.id,"name":emp.name,"department":emp.department, "salary":emp.salary,"location":emp.location,"age":emp.age,"experience":emp.experience}for emp in qs]

         return JsonResponse({"data":result,"status":"200 ok"})
    
    def post(self,request,*args,**kwargs):
         
         data = loads(request.body)

         qs = Employee.objects.create(
              
              name = data.get("name"),

              department = data.get("department"),

              salary = data.get("salary"),

              location = data.get("location"),

              age = data.get("age"),

              experience = data.get("experience")

         )

         return JsonResponse({"data":"record inserted","status":"200 success"})
    
@method_decorator(csrf_exempt,name="dispatch")    
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = Employee.objects.get(id=id)

        result =[{"id":qs.id,"name":qs.name,"department":qs.department,"salary":qs.salary,"location":qs.location,"age":qs.age,"experience":qs.experience}]

        return JsonResponse({"data":result,"status":"200 ok"})
    
    def delete(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return JsonResponse({"data":"deleted","status":"200 ok"})
    
    def put(self,request,*args,**kwargs):

        id= kwargs.get("pk")

        data = loads(request.body)

        Employee.objects.filter(id=id).update(**data)

        return JsonResponse({"data":"updated","status":"200 ok"})
    

