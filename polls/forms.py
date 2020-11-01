from django import forms

class UserForm(forms.Form):
     word = forms.CharField()
     name = forms.CharField(label='名前', max_length=100)