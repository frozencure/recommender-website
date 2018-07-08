from django import forms
from django import forms

class QuestionForm(forms.Form):
    userName = forms.CharField(label='', max_length=50)