from django import forms
from iotoiletapp.models import Floor, Sex, Room


class IotoiletappForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('user_name', 'email', 'sex', 'job', 'inquiry_text')
        widgets = {
            'user_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'sex': forms.RadioSelect(),
            'job': forms.Select(attrs={"class": "form-control"}),
            'inquiry_text': forms.Textarea(attrs={"class": "form-control", "cols": "10",  "rows": "4"}),
        }