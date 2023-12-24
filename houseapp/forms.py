from django import forms
from .models import HouseModel

class HouseDateForm(forms.ModelForm):
	class Meta:
		model = HouseModel
		fields = ['testfile', 'area', 'distance']
		widgets = {
			'testfile': forms.FileInput(attrs={'class':'form-control'}),
			'area': forms.NumberInput(attrs={'class':'form-control'}),
			'distance': forms.NumberInput(attrs={'class':'form-control'}),
		}
	
