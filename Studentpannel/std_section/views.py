from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def create_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        Password = make_password(request.POST["password"])

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