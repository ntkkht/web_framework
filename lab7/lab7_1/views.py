from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import VideoSerializer
from .models import Video
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_page(request):
    return render(request, "video.html")

@api_view(['GET'])
def get_video(request):
    print("TEST")
    video = Video.objects.all()
    return Response(VideoSerializer(video, many=True).data)

@csrf_exempt
@api_view(['POST'])
def post_video(request):
    print("Received POST data:", request.data)
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)