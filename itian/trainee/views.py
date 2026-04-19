# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Trainee
# # Create your views here.

# def listtrainee(request):
#     return HttpResponse('List of trainees')

# def addtrainee(request):
#     return HttpResponse('Add a new trainee')

# def updatetrainee(request,id):
#     trainee = Trainee.objects.get(id=id)
#     return HttpResponse(f'Update trainee with id {id}')

# def deletetrainee(request,id):
#     trainee = Trainee.objects.get(id=id)
#     return HttpResponse(f'Delete trainee with id {id}')

# def gettraineebyid(request,id):
#     trainee = Trainee.objects.get(id=id)
#     return HttpResponse(f'Trainee details for id {id}')
# ---------------------------------------------------------------------

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