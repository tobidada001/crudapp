from django.shortcuts import render, redirect
from .models import Employee
# Create your views here.



def index(request):

    if request.method == 'POST':
        firstname =  request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pword']

        emp = Employee(firstname = firstname, lastname = lastname, email = email, password = password)
        emp.save()
        print('Data is inserted!!')
        return redirect('/')
    return render(request, "index.html")

def details(request):

    emp = Employee.objects.all()
    
    return render(request, "details.html", {"emps": emp})



def signin(request):
    

    if request.method == 'POST':
        eml = request.POST['email']
        pword = request.POST['password']
        emp = Employee.objects.filter(email = eml, password = pword)
        print(emp)
        
        if(emp.exists()):
            print(emp," exists!!!!!")
            return redirect('/home')
        else:
            print(emp, " does not exist!!!")
            return redirect('/signin')
    return render(request, "signin.html")

def home(request):
    return render(request, "home.html")


def error(request):
    return render(request, "error.html")




