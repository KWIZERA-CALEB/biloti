from django.urls import path
from . import views

urlpatterns = [
    path('add-class/', views.addClass, name='add-class'),
    path('add-school-year', views.addSchoolYear, name='add-school-year'),
    path('school-year/<str:pk>/', views.renderSchoolYear, name='school-year'),
    path('school-term/<str:pk>/', views.renderTerm, name='term')
]