from typing import Any, Dict
from django.shortcuts import render, redirect
from myapp.models import Student,StudentProfile,ClassRoom
from django.db import transaction
from .forms import StudentForm,StudentModelForm
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

# Create your views here.
transaction.atomic
def template_form(request):
    print(request.method)
    classroom=ClassRoom.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')
        classroom = request.POST.get('classroom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pp = request.FILES.get('image')
        print(classroom)
        # classroom_id = ClassRoom.objects.get(name=classroom)
        # print(classroom_id)
        classroom_obj = ClassRoom.objects.get(id=classroom) 
        # print(classroom_obj.id)
        try: classroom_obj = ClassRoom.objects.get(id=classroom)
        except: Classroom_obj = None
    
        stu = Student.objects.create(name=name,age=age,department=department,classroom=classroom_obj)
        StudentProfile.objects.create(email=email,address=address,phone=phone,image=pp,student=stu)
        return redirect('stu')

    context={
        "title":"form Student",
        "classroom":classroom
    }
    return render(request, "form/template_form.html", context)

@login_required
def student_detail(request,id):
    try:
        stu = Student.objects.get(id=id)
    except:
        pass
    print(stu)
    return render(request, 'form/stu_details.html',{'stu': stu})

def student_update(request,id):
    stu = Student.objects.get(id=id)
    classroom = ClassRoom.objects.all()
    print('stu', stu)

    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')
        classroom = request.POST.get('classroom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pp = request.FILES.get('image')
        classroom_obj = ClassRoom.objects.get(id=classroom) 
        # print(classroom_obj.id)
        try: classroom_obj = ClassRoom.objects.get(id=classroom)
        except: Classroom_obj = None
        stu = Student.objects.filter(id=id).update(name=name,age=age,department=department)
        try:
            sp  = StudentProfile.objects.get(student_id=id)
            print('sp',sp)
            sp.email=email
            sp.address=address
            sp.phone=phone
            if pp:
                print(pp)
                sp.image=pp
            sp.save()
        except:
            StudentProfile.objects.create(student_id=id,email=email,address=address,phone=phone,image=pp)

        

            
        return redirect('stu')

    return render(request, 'form/stu_update.html',{'stu': stu, 'classroom':classroom})


def student_form(request):
    if request.method =="POST":
        form = StudentForm(request.POST) # It gives raw data querydict
        print(request.POST)
        if form.is_valid():
            # print(form.cleaned_data) #it gives cleaned data in dict that can be store in database
            # name = form.cleaned_data.get('name')
            # age = form.cleaned_data.get('age')
            # department = form.cleaned_data.get('department')
            # Student.objects.create(name=name,age=age,department=department) OR,
            Student.objects.create(**form.cleaned_data)
            return redirect('stu')
        
    form=StudentForm()
    return render(request,'form/student_form.html', {'form':form})

def student_modelform(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('stu')
    form = StudentModelForm()
    return render(request, "form/student_modelform.html", {'form':form})

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = "form/student_create.html"
    success_url = reverse_lazy("stu")

class StudentTemplateView(TemplateView):
    template_name ="myapp/stu.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']='StudentTemplateView'
        return context
    
# @method_decorator(login_required)  if we use decoratorlikethis rather than in URL we must give name 
@method_decorator(login_required, name="dispatch") 
class StudentListView(ListView):
    model = Student
    template_name="myapp/stu.html"
    context_object_name="students"