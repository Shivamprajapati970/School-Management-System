from django.shortcuts import render,HttpResponse, redirect
from .models import *
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    return render(request,"index.html")

def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password=request.POST["password"]
        Password = make_password(request.POST["password"])
        if Student.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            Student.objects.create(name=name,email=email,password=password)
            return HttpResponse("Student created successgully.")

def profile(request):
    return render(request,"profile.html")

def sign_up(request):
    return render(request,"sign-up.html")


def dashboard(request):
    return render(request,"dashboard.html")

def viewstudents(request):
    return render(request,"viewstudents.html")

def courses(request):
    return render(request,"courses.html")

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