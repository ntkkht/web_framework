from django.shortcuts import redirect, render
from .forms import LoginForm
from .models import Member, Video, Author
def logout(request):
    try:
        del request.session["username"]
    except KeyError:
        pass
    return redirect("/login/")
def login_fill(request):
    try:
        request.session["username"]
        return redirect('/showvideo/')
    except KeyError:
        pass
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                member = Member.objects.get(username=username, password=password)
                request.session["username"] = member.username
                return redirect("/showvideo/")
            except Exception as e:
                pass
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
def showvideo(request):
    try:
        request.session["username"]
    except KeyError:
        return redirect('/login/')
    videos = Video.objects.all().values()
    return render(request, "showvideo.html", { "videos": videos })
def showauthor(request, id):
    try:
        request.session["username"]
    except KeyError:
        return redirect('/login/')
    if not id:
        return redirect("/showvideo/")
    author = Author.objects.get(id=id)
    return render(request, "showauthor.html", { "author": author })