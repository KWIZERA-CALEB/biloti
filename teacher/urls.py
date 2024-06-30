from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.addStudent, name='add-student'),
    path('classes/', views.classes, name='classes'),
    path('class/<str:pk>/', views.classroom, name='class'),
    path('student-portal/<str:pk>/', views.student, name='student'),
    path('generate-report/<str:pk>/', views.generateDoc, name='generate-report'),
    path('', views.home, name='home'),
    

]