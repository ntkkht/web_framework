from django.shortcuts import render
from .forms import CitizenForm
from django.http import HttpResponse
# Create your views here.

def createCitizen(request):
    if request.method == "POST":
        form = CitizenForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks....Save form already.')
        else:
            return HttpResponse(form.errors.as_text())
        
    return render(request, "createCitizen.html", {"form": CitizenForm()})