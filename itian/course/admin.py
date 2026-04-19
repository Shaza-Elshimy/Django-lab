from django.contrib import admin

from course.models import Course
from trainee.models import  Trainee

# Register your models here.
admin.site.register(Course)
admin.site.register(Trainee)