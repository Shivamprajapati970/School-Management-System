from django.shortcuts import render,HttpResponse, redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def index(request):
    return render(request,"index.html")

def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        #password=request.POST["password"]
        password = make_password(request.POST["password"])
        if Student.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            Student.objects.create(name=name,email=email,password=password)
            return redirect("/")

def profile(request):
    return render(request,"profile.html")

def sign_up(request):
    return render(request,"sign-up.html")


def dashboard(request):
    return render(request,"dashboard.html")

def viewstudents(request):
    course_obj=Course.objects.all()
    return render(request,"viewstudents.html",{"course_obj":course_obj})

'''def data(request):
    user_obj=User.objects.all()
    return render(request,"table.html",{"user_obj":user_obj})'''

def courses(request):
    course_obj=Course.objects.all()
    return render(request,"courses.html",{"course_obj":course_obj})

def add_courses(request):
    if request.method=="POST":
        course_name=request.POST["corses"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        if Course.objects.filter(course_name=course_name).exists():
            return HttpResponse("Course already exists.")
        else:
            Course.objects.create(course_name=course_name,fees=fees,duration=duration)
            return redirect("/courses/")
        
def sign_in(request):
    if request.method=="POST":
        email=request.POST['email']
        user_password=request.POST['password']
        if Student.objects.filter(email=email).exists():
            obj=Student.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/dashboard/')
            else:
                 return HttpResponse("Password incorrect.")
        else:
            return HttpResponse("email not registered.")
        
def delete_course(request, pk):
    Course.objects.get(id=pk).delete()
    return redirect("/courses/")

def update_course(request, uid):
    course=Course.objects.get(id=uid)
    return render(request,"update_course.html",{'course':course})

def course_update(request):
    if request.method == "POST":
        uid=request.POST['uid']
        course_name=request.POST['corses']
        fees=request.POST['fees']
        duration=request.POST['duration']
        Course.objects.filter(id=uid).update(course_name=course_name,fees=fees,duration=duration)
        return redirect('/courses/')
        