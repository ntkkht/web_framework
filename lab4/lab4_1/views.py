from django.shortcuts import render
from django.views import View
from .models import Video, Course
# Create your views here.

class show_video(View):
    def get(self, request, *args, **kwargs):
        video_title = self.kwargs.get("video_title")
        videos = Video.objects.filter(title__contains=video_title)
        return render(
            request=request, 
            template_name="videos.html", 
            context={
                "video_title": video_title, 
                "videos": videos 
            })
    
class show_coursevideo(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get("course_id")
        course = Course.objects.get(id=course_id)
        videos = course.video.all() 
        return render(
            request=request, 
            template_name="course.html", 
            context={
                "course_id": course_id, 
                "course": course, 
                "videos": videos 
            })