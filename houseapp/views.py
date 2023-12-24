from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from houseapp.forms import HouseDateForm
from .functions import house_price_pre

# 機械学習のためのimport
import csv,io
import math
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
			input_area = request.POST['area']
			input_distance = request.POST['distance']
			result_data = house_price_pre(df, input_area,input_distance)
			msg = '予測出来ました。'
		title = 'Prediction result'
		form = HouseDateForm(request.POST)
		submit = '再予測'
		displayflg = 1
	else:
		title = 'House price prediction'
		form = HouseDateForm()
		submit = '予測'
		result_data = {}
		msg = 'test_message'
		displayflg = 0
	params = {
		'title' : title,
		'form' : form,
		'submit': submit,
		'data': result_data,
		'message': msg,
		'displayflg': displayflg,
	}
	return render(request, 'house.html', params)