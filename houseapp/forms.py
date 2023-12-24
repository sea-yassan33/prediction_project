from django import forms

class HouseDateForm(forms.Form):
	testfile = forms.FileField(label='賃貸価格データ(csv)', widget=forms.FileInput(attrs={'class':'form-control'}))
	area = forms.IntegerField(label='賃貸の広さ(㎡)', widget=forms.NumberInput(attrs={'class':'form-control'}))
	distance = forms.IntegerField(label='駅からの距離(m)', widget=forms.NumberInput(attrs={'class':'form-control'}))