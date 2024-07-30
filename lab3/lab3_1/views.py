import datetime
from django.shortcuts import render

from .forms import VideoForm, AuthorForm
from .models import Author, Video

def handle_video_request(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            Video(
                title=form.data.get('title'), 
                published_date=datetime.datetime.now(), 
                short_detail=form.data.get('short_detail'), 
                demo= True if form.data.get('demo') == 'on' else False
            ).save()
        
    video = [ d.getData() for d in Video.objects.all() ]
        
    return render(request=request, template_name="video.html", context={"form": VideoForm(), 'data': video })

def handle_author_request(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print()
            Author(
                firstname=form.data.get('firstname'), 
                lastname=form.data.get('lastname'), 
                phone=form.data.get('phone'), 
                type_author=form.data.get('type_author'), 
                joined_date=datetime.datetime.now()
            ).save()
            
    authors = [ d.getData() for d in Author.objects.all() ]
    
    return render(request=request, template_name="author.html", context={"form": AuthorForm(), 'data': authors})