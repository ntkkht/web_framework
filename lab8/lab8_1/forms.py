from django import forms
from django.core.exceptions import ValidationError
from lab8_1.models import Citizen
from datetime import date
from django.forms import DateInput, ModelForm, TextInput, Select
from django.utils.translation import gettext_lazy as _

class CitizenForm(ModelForm):
    citizenId = forms.CharField(max_length=13, widget=TextInput())
    firstname = forms.CharField(max_length=256, widget=TextInput())
    lastname = forms.CharField(max_length=256, widget=TextInput())
    expire_date = forms.DateField(widget=DateInput(attrs={"format": "%Y-%m-%d"}))
    blood_type = forms.ChoiceField(widget=Select, choices=[("A", "A"), ("B", "B"), ("AB","AB"), ("O","O")])
    class Meta:
        model = Citizen
        fields = [
            "citizenId", 
            "firstname",
            "lastname",
            "expire_date",
            "blood_type"
        ]
    def clean(self):
        super(CitizenForm, self).clean()
        citizenId = self.cleaned_data.get("citizenId")
        firstname = self.cleaned_data.get("firstname")
        lastname = self.cleaned_data.get("lastname")
        expire_date = self.cleaned_data.get("expire_date")
        blood_type = self.cleaned_data.get("blood_type")
        if citizenId[0] == '0':
            raise ValidationError(_("Citizen id must not start with 0"))
        if len(citizenId) != 13:
            raise ValidationError(_("Citizen id must be 13 digit"))
        if firstname == lastname:
            raise ValidationError(_("Firstname and lastname must not be the same"))
        if blood_type not in ['A', 'B', 'AB', 'O']:
            raise ValidationError(_("Blood type is invalid"))
        if expire_date < date.today():
            raise ValidationError(_("Invalid date"))
        return self.cleaned_data