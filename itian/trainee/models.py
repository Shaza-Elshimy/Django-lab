from django.db import models
from course.models import Course
from django.core.exceptions import ValidationError
# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def validate_age(self,value):
        if value < 21:
            raise ValidationError("Minimum age is 15")
        return value
