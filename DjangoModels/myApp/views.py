from django.shortcuts import render
from myApp.models import Employee
def view1(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'myApp/1.html',d)
