
from django.urls import path

from .views import *

urlpatterns=[
    path('',listtrainee,name='trainee_list'),
    path('add/',AddTraineeView.as_view(),name='trainee_add'),
    path('<int:id>/update/',UpdateTraineeView.as_view(),name='trainee_update'),
    path('<int:pk>/delete/',DeleteTraineeView.as_view(),name='trainee_delete'),
    path('<int:id>/',gettraineebyid,name='trainee_details'),
]
