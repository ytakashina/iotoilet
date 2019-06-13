from django import forms

SEX_CHOICES = [
    (1, '男'),
    (2, '女'),
]

FLOOR_CHOICES = [
    (1, '25階'),
    (2, '26階'),
    (3, '27階'),
    (4, '28階'),
    (5, '29階'),
]


class IotoiletappForm(forms.Form):
    sex = forms.ChoiceField(label='性別', choices=SEX_CHOICES, initial=1)
    floor = forms.ChoiceField(label='フロア', choices=FLOOR_CHOICES, initial=1)
