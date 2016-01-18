from django import forms
# Create your views here.

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
