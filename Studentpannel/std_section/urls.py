from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("profile/",profile),
    path("sign_up/",sign_up),
    path("dashboard/",dashboard),
    path("viewstudents/",viewstudents),
    path("courses/",courses),
#
    path("registration/",create_student),
    path("add_courses/",add_courses),
    path("sign_in/",sign_in),
    path("delete_course/<int:pk>/",delete_course,name="delete"),
    
    path("course_update/<int:uid>/",update_course,name="course_update"),
    path("update_course/",course_update),
]
