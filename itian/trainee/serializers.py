from rest_framework import serializers
from .models import Trainee

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Trainee
        fields='__all__'

    def validate_age(self,value):
        if value < 21:
            raise serializers.ValidationError("Minimum age is 15")
        return value