from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import HouseDateForm
from .forms import HouseListForm
from .functions import house_price_pre
from .functions import path_flag
from .functions import house_list_pre

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
	msg = ''
	errormsg = ''
	displayflg = 0
	if(request.method == 'POST'):
		upload = HouseDateForm(request.POST, request.FILES)
		input_area = int(request.POST['area'])
		input_distance = int(request.POST['distance'])
		#アップロードされたファイル形式を判定
		filename = str(request.FILES['testfile'])
		file_flag = path_flag(filename)
		#入力値が正しくない場合
		if input_area <= 0 or input_area >= 10000 or input_distance <= 0 or input_distance >= 100000 or file_flag == 0:
			errormsg = "入力値が正しくありません。"
			result_data = {}
			msg = 'test_message'
		#機械学習の処理
		elif upload.is_valid():
			df = pd.read_csv(io.StringIO(request.FILES['testfile'].read().decode('utf-8')), delimiter=',')
			result_data = house_price_pre(df, input_area,input_distance)
			msg = 'Made a prediction.'
			displayflg = 1
		submit = '再予測'
		form = HouseDateForm(request.POST, request.FILES)
	else:
		form = HouseDateForm()
		submit = '予測'
		result_data = {}
		msg = 'test_message'
	params = {
		'title' : '住宅価格(モデルデータセット)',
		'errormsg': errormsg,
		'form' : form,
		'submit': submit,
		'data': result_data,
		'message': msg,
		'displayflg': displayflg,
	}
	return render(request, 'house.html', params)

def houselist(request):
	msg = ''
	errormsg = ''
	displayflg = 0
	if(request.method == 'POST'):
		upload = HouseListForm(request.POST, request.FILES)
		#アップロードされたファイル形式を判定
		filename = str(request.FILES['testfile'])
		file_flag = path_flag(filename)
		#入力値が正しくない場合
		if file_flag == 0:
			errormsg = "入力値が正しくありません。"
			result_data = {}
			msg = 'test_message'
		#機械学習の処理
		elif upload.is_valid():
			df = pd.read_csv(io.StringIO(request.FILES['testfile'].read().decode('utf-8')), delimiter=',')
			result_data = house_list_pre(df)
			msg = 'Made a prediction.'
			displayflg = 1
		submit = '再予測'
		form = HouseListForm(request.POST, request.FILES)
	else:
		form = HouseListForm()
		submit = '予測'
		result_data = {}
		msg = 'test_message'
	params = {
		'title' : '住宅価格(予測データセット)',
		'errormsg': errormsg,
		'form' : form,
		'submit': submit,
		'data': result_data,
		'message': msg,
		'displayflg': displayflg,
	}
	return render(request, 'houselist.html', params)