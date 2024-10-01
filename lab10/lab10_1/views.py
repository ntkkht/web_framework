from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Student, Teacher, Person

class person_list(ListView):
    model = Person

class student_list(ListView):
    model = Student
    
class teacher_list(ListView):
    model = Teacher
    
class member_list(TemplateView):
    template_name = "member_list.html"
    model = Person
    extra_context={'members': Person.objects.all()}