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

from urllib import request

from django.shortcuts import redirect, render
from django.views import View
from .models import *
# Create your views here.
# function based
def listtrainee(request):
    trainees = Trainee.objects.all()
    return render(request,'trainee_list.html', {'trainees': trainees})

# def addtrainee(request):
#     courses=Course.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         courses_ids = request.POST.getlist('course')
#         trainee = Trainee.objects.create(name=name, age=age)
#         trainee.course.set(courses_ids)
        
#         return redirect('trainee_list')
#     return render(request,'trainee_add.html', {'courses': courses})

#class based + model form
class AddTraineeView(View):
    def get(self,request):
        courses=Course.objects.all()
        return render(request,'trainee_add.html', {'courses': courses})
    
    def post(self,request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        courses_ids = request.POST.getlist('course')
        trainee = Trainee.objects.create(name=name, age=age)
        trainee.course.set(courses_ids)
        return redirect('trainee_list')
        
# def updatetrainee(request,id):
#     trainee = Trainee.objects.get(id=id)
#     courses=Course.objects.all()
#     if request.method == 'POST':
#         trainee.name = request.POST.get('name')
#         trainee.age = request.POST.get('age')
#         courses_ids = request.POST.getlist('course')
#         trainee.course.set(courses_ids)
#         trainee.save()
#         return redirect('trainee_list')
#     return render(request,'trainee_update.html', {'trainee': trainee, 'courses': courses})

#class based

    
def deletetrainee(request,id):
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request,'trainee_delete.html', {'trainee': trainee})
# function based
def gettraineebyid(request,id):
    trainee = Trainee.objects.get(id=id)
    return render(request,'trainee_details.html', {'trainee': trainee})