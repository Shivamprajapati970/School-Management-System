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
    
]
