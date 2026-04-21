from rest_framework import selializers
from .models import Trainee

class TraineeSerializer(selializers.ModelSerializer):
    class Meta:
        model =Trainee
        fields='__all__'