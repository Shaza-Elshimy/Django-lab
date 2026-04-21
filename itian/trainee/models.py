from django.db import models
from course.models import Course
# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.name