from django import forms

class AuthorForm(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=255)
    lastname = forms.CharField(label="lastname", max_length=255)
    phone = forms.CharField(label="phone", max_length=10)
    type_author = forms.ChoiceField(label="type", choices= [("A", "Fulltime"), ("B", "Parttime")])


class VideoForm(forms.Form):
    title = forms.CharField(label="title", max_length=50)
    short_detail = forms.CharField(label="short_detail", max_length = 300)
    demo = forms.BooleanField(label="demo", initial= False)
