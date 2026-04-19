from django.shortcuts import render

from .models import Trainee
# Create your views here.

def listtrainee(request):
    trainees = Trainee.objects.all()
    return render(request,'trainee_list.html', {'trainees': trainees})

def addtrainee(request):
    return render(request,'trainee_add.html')

def updatetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    return render(request,'trainee_update.html', {'trainee': trainee})

def deletetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    return render(request,'trainee_delete.html', {'trainee': trainee})

def gettraineebyid(request,id):
    trainee = Trainee.objects.get(id=id)
    return render(request,'trainee_detail.html', {'trainee': trainee})