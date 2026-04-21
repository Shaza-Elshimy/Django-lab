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

from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from .models import *
from .forms import TraineeForm
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.
# function based
def listtrainee(request):
    # trainees = Trainee.objects.all()
    trainees=Trainee.objects.filter(is_deleted=False)
    deleted_trainees=Trainee.objects.filter(is_deleted=True)
    return render(request,'trainee_list.html', {'trainees': trainees,'deleted_trainees':deleted_trainees})

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
        # courses=Course.objects.all()
        form = TraineeForm()
        return render(request,'trainee_add.html',{'form':form})
    
    def post(self,request):
        # name = request.POST.get('name')
        # age = request.POST.get('age')
        # courses_ids = request.POST.getlist('course')
        # trainee = Trainee.objects.create(name=name, age=age)
        # trainee.course.set(courses_ids)
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
        return render(request,'trainee_add.html',{'form':form})

    
        
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
class UpdateTraineeView(View):
    def get(self,request,id):
        trainee = Trainee.objects.get(id=id)
        courses=Course.objects.all()
        return render(request,'trainee_update.html', {'trainee': trainee, 'courses': courses})
    def post(self,request,id):
        trainee=get_object_or_404(Trainee,id=id)
        trainee.name = request.POST.get('name')
        trainee.age = request.POST.get('age')
        courses_ids = request.POST.getlist('course')
        trainee.course.set(courses_ids)
        trainee.save()
        return redirect('trainee_list')
        


    
        
    
# def deletetrainee(request,id):
#     trainee = Trainee.objects.get(id=id)
#     if request.method == 'POST':
#         trainee.delete()
#         return redirect('trainee_list')
#     return render(request,'trainee_delete.html', {'trainee': trainee})

# generic 
# class DeleteTraineeView(DeleteView):
#     model =Trainee
#     template_name ='trainee_delete.html'
#     success_url=reverse_lazy('trainee_list')

#    soft delete 
class DeleteTraineeView(UpdateView):
    model =Trainee
    fields=[]
    template_name ='trainee_delete.html'
    success_url=reverse_lazy('trainee_list')
    def form_valid(self,form):
        self.object.is_deleted=True
        self.object.save()
        return super().form_valid(form)

# function based
def gettraineebyid(request,id):
    trainee = Trainee.objects.get(id=id)
    return render(request,'trainee_details.html', {'trainee': trainee})