
from django.urls import path

from .views import *

urlpatterns=[
    path('',listtrainee,name='trainee_list'),
    path('add/',addtrainee,name='trainee_add'),
    path('<int:id>/update/',updatetrainee,name='trainee_update'),
    path('<int:id>/delete/',deletetrainee,name='trainee_delete'),
    path('<int:id>/',gettraineebyid,name='trainee_details'),
]