from datetime import date
from .models import Author

from django.forms import DateInput, ModelForm, TextInput

class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ["id","firstname", "lastname", "phone", "joined_date"]

        today = date.today()

        widgets= {
            "id": TextInput(attrs={"size": 30 }),
            "firstname": TextInput(attrs={"size": 30 }),
            "lastname": TextInput(attrs={"size": 30 }),
            "phone": TextInput(attrs={"size": 30 }),
            "joined_date" : DateInput(attrs={"format": "%Y-%m-%d", "value": today}),
        }