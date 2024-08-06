from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import BadRequest
from .models import Author
from .forms import AuthorForm
from django.forms import modelformset_factory
from django.shortcuts import render

def authorformset(request):
    AuthorFormSet = modelformset_factory(Author, form = AuthorForm , extra=2)
    if request.method == "POST":
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Thanks....Save formset already.') #This can be template
        else:
            raise BadRequest('bad req')
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(firstname__startswith='A'))
    return render(request, "addauthors.html", {"formset": formset})

def get_author(request):
    form = AuthorForm(instance=Author.objects.filter(firstname__startswith='A').order_by('firstname').first())
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks....Save formset already.') #This can be template
    authors = Author.objects.filter(firstname__startswith='A').order_by('firstname')
    return render(request, 'get_author.html', {'form': form, 'authors': authors})

def get_author_by_video(request):
    form = AuthorForm(instance=Author.objects.filter(video__title__startswith='A').first())
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks....Save formset already.') #This can be template
    authors = Author.objects.filter(video__title__startswith='A')
    # for author in authors:
    #     print(author)
    return render(request, 'get_author.html', {'form': form, 'authors': authors})