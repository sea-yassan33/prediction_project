from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from houseapp.forms import HouseDateForm

# 機械学習のためのimport
import csv,io
import pandas as pd

def index(request):
	params = {
		'title' : 'Table Of Contents',
	}
	return render(request, 'index.html', params)

def house(request):
	if(request.method == 'POST'):
		msg = 'test0'
		upload = HouseDateForm(request.POST, request.FILES)
		if upload.is_valid():
			df = pd.read_csv(io.StringIO(request.FILES['testfile'].read().decode('utf-8')), delimiter=',')
			msg = 'test2'
		title = 'Prediction result'
		form = HouseDateForm(request.POST)
		submit = '再予測'
	else:
		title = 'House price prediction'
		form = HouseDateForm()
		submit = '予測'
		msg = 'test_message'
	params = {
		'title' : title,
		'form' : form,
		'submit': submit,
		'message': msg,
	}
	return render(request, 'house.html', params)