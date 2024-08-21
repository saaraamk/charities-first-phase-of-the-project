from django.urls import path

from . import views

urlpatterns = [
    path('benefactors/', views.BenefactorRegistration.as_view()),
    path('charities/', views.CharityRegistration.as_view()),
    path('tasks/', views.Tasks.as_view()),
    path('tasks/<int:task_id>/request/', views.TaskRequest.as_view()),
    path('tasks/<int:task_id>/response/', views.TaskResponse.as_view()),
    path('tasks/<int:task_id>/done/', views.DoneTask.as_view()),
    path('task-request/<int:task_id>/', views.TaskRequest.as_view(), name='task-request'),
    path('task-response/<int:task_id>/', views.TaskResponse.as_view(), name='task-response'),
    path('tasks/<int:task_id>/done/', views.DoneTask.as_view(), name='done-task'),

]
