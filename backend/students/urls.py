from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.student_form, name='student_form'),
    path('list/', views.student_list, name='student_list'),
]