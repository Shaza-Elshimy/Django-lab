from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.

def listtrainee(request):
    return HttpResponse('List of trainees')

def addtrainee(request):
    return HttpResponse('Add a new trainee')

def updatetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    return HttpResponse(f'Update trainee with id {id}')

def deletetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    return HttpResponse(f'Delete trainee with id {id}')

def gettraineebyid(request,id):
    trainee = Trainee.objects.get(id=id)
    return HttpResponse(f'Trainee details for id {id}')