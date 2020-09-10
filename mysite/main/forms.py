from django import forms

# Create your forms here


class CreateNewList(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    check = forms.BooleanField(required=False)
