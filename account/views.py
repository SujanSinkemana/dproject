
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate
from django.views.generic import View

def user_login(request):
    if request.method == "POST":
        print(request.POST)
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(request,username=un, password=pw)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('stu')
            print("login")
        else:
            
            return redirect("login")
    return render(request,'account/login.html' )

def user_logout(request):
    logout(request)
    return render(request,'account/login.html')
    

def newfun(request, template_name):
    template_name=template_name
    context ={'info': 'This is Functionbasre tempalte'}
    return render(request,template_name,context)

class NewClassView(View):
    template_name='account/temp.html'
    def get(self,request):
        context ={'info': 'This is classbasre tempalte'}
        return render(request,self.template_name,context)
        

class NewClassView1(View):
    template_name=''
    def get(self,request):
        context ={'info': 'This is classbasre tempalte'}
        return render(request,self.template_name,context)
        
