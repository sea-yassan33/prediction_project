from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import HouseDateForm
from .forms import HouseListForm
from .forms import ImgUploadForm
from .functions import house_price_pre
from .functions import path_flag
from .functions import img_flag
from .functions import house_list_pre
from .functions import obj_detec
# 機械学習のためのimport
import io
import pandas as pd
import base64
from PIL import Image

#index
def index(request):
	params = {
		'title' : 'Table Of Contents',
	}
	return render(request, 'index.html', params)

#賃貸価格(モデルデータセット)
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
		#入力値のチェック
		if input_area <= 0 or input_area >= 10000 or input_distance <= 0 or input_distance >= 100000 or file_flag == 0:
			#入力値が規定範囲外、もしくはfile_flagが0の場合
			errormsg = "入力値が正しくありません。"
			result_data = {}
			msg = 'test_message'
		elif upload.is_valid():
			#機械学習の処理
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
		'title' : '賃貸価格(モデルデータセット)',
		'errormsg': errormsg,
		'form' : form,
		'submit': submit,
		'data': result_data,
		'message': msg,
		'displayflg': displayflg,
		'modalMaeText': '絶対値誤差平均（MAE：Mean Absolute Error）は、予測値と実測値の誤差の絶対値の平均である。各データに対して誤差の絶対値を取り、誤差の絶対値を合計し、最後にデータの件数で割って平均を取る。予測精度は0に近いほど高いと言える。',
		'modalR2Text': '決定係数について<hr>【決定係数】：【精度】<br>0.8以上:非常に良い<br>0.5以上:良い<br>0.25以上:やや良い<br>0.25未満:良くない',
	}
	return render(request, 'house.html', params)

# 賃貸価格(予測データセット)
def houselist(request):
	msg = ''
	errormsg = ''
	displayflg = 0
	if(request.method == 'POST'):
		upload = HouseListForm(request.POST, request.FILES)
		#アップロードされたファイル形式を判定
		filename = str(request.FILES['testfile'])
		file_flag = path_flag(filename)
		if file_flag == 0:
			#ファイル形式が正しくない場合
			errormsg = "入力値が正しくありません。"
			result_data = {}
			msg = 'test_message'
		elif upload.is_valid():
			#機械学習の処理
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
		'title' : '賃貸価格(予測データセット)',
		'errormsg': errormsg,
		'form' : form,
		'submit': submit,
		'data': result_data,
		'message': msg,
		'displayflg': displayflg,
	}
	return render(request, 'houselist.html', params)

#物体検知
def imgReco(request):
	msg = ''
	errormsg = ''
	image_data = ''
	result_data = ''
	displayflg = 0
	submit = ''
	if(request.method == 'POST'):
		form = ImgUploadForm(request.POST, request.FILES)
		#アップロードされたファイル形式を判定
		filename = str(request.FILES['image'])
		file_flag = img_flag(filename)
		if file_flag == 0:
			#ファイル形式が正しくない場合
			errormsg = "png形式もしくはjpg形式をアップロードして下さい。"
			result_data = {}
			msg = 'test_message'
		elif form.is_valid():
			#機械学習実施
			#アップロードされた画像をBase64文字列に変換
			image_data = base64.b64encode(request.FILES['image'].read()).decode('utf-8')
			#アップロードされた画像を機械学習用に取り込む
			img = Image.open(request.FILES['image'])
			#物体検知処理
			result_data = obj_detec(img)
			displayflg = 1
		submit = '再予測'
	else:
		form = ImgUploadForm()
		submit = '予測'
	params = {
		'title' : '物体検知',
		'errormsg': errormsg,
		'form' : form,
		'submit': submit,
		'imgdata': image_data,
		'imgresalt': result_data,
		'message': msg,
		'displayflg': displayflg,
	}
	return render(request, 'imgreco.html', params)