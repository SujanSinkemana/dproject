from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student, ClassRoom, StudentProfile
from .forms import StudentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, "myapp/index.html")

def port(request):
    return render(request, "myapp/port.html")

def test(request):
    return render(request, "myapp/test.html")

def page1(request):
    context = {
        "students":[{"name":"Ram", "age":20, "department":"IT"},
                    {"name":"sita", "age":21, "department":"IT"},
                    {"name":"gita", "age":22, "department":"IT"}]
    }
    print(type(context))
    return render(request, "myapp/page1.html", context=context)

def page2(request):
    students = Student.objects.all()
    context = {'students':students}
    print(type(students))
    
    return render(request, "myapp/page2.html", context)

@login_required
def class_info(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ""
    classes =ClassRoom.objects.all()
    students = Student.objects.filter(
        Q(name__icontains=q)|
        Q(classroom__name__icontains=q)|
        Q(department__icontains=q)|
        Q(age__icontains=q)
        )
        
    students_profile =StudentProfile.objects.all()
    context = {'classes':classes,'students':students, 'students_profile':students_profile}
    return render(request, "myapp/stu.html", context)

def studentform(request):
    form=StudentForm()
    if request.method=="POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        department =request.POST.get("department")
        classroom = request.POST.get("classroom")
        classroom_create, created = ClassRoom.objects.get_or_create(name=classroom)
        # print(classroom_create, created)
        stu = Student.objects.create(name=name,age=age,department=department,classroom=classroom_create)
        return redirect('stu')
    return render(request, "myapp/form.html")