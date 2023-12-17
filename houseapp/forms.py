from django import forms

class HouseDateForm(forms.Form):
	testfile = forms.FileField(label='date', widget=forms.FileInput(attrs={'class':'form-control'}))