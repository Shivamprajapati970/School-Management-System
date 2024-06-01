from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)

class Course(models.Model):
    course_name=models.CharField(max_length=200)
    fees=models.IntegerField()
    duration=models.CharField(max_length=100)


class Student_detail(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    mobile_no=models.CharField(max_length=13)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    