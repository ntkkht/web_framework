from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Author, Video

def video(request):
  videos = Video.objects.all().values()
  template = loader.get_template('video_list.html')
  context = {
    'videos': videos,
  }
  return HttpResponse(template.render(context, request))

def author(request):
  authors = Author.objects.all().values()
  template = loader.get_template('author_list.html')
  context = {
    'authors': authors,
  }
  return HttpResponse(template.render(context, request))