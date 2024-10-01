"""
URL configuration for lab10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from lab10_1.views import student_list, teacher_list, person_list, member_list

urlpatterns = [
    path('person/', person_list.as_view()),
    path('student/', student_list.as_view()),
    path('teacher/', teacher_list.as_view()),
    path('member/', member_list.as_view()),
]
