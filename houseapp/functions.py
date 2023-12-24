# モジュールのインポート
import math
import os
import pandas as pd
# Ridge Regressionモデルクラスの読み込み
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
# scikit-learnの準備
from sklearn.model_selection import train_test_split
# 線形回帰で学習
from sklearn import linear_model

# 住宅価格関数
def house_price_pre(df,input_area, input_distance):
	#特徴量と正解データの設定
	## 使いたい特徴量
	feature_cols = ['house_area','distance']
	## 予測したい列
	target_col = 'rent_price'
	x = df[feature_cols]
	y = df[target_col]

	# 訓練データとテストデータに8:2で分割
	X_train, X_test, y_train, y_test = train_test_split(x, y, 	test_size=0.2, random_state=0)
	# モデル学習
	model = linear_model.LinearRegression()
	model.fit(X_train, y_train)
	# 学習したモデルを用いて予想
	df['pred_rent_price'] = model.predict(x)

	# 訓練データを用いた評価
	model_ases = model.score(X_train, y_train)

	# MAE(平均絶対値誤差)
	## 正解値と予測値の差の絶対値で平均値を取ったもの
	err_range = mean_absolute_error(df['rent_price'],df	['pred_rent_price'])

	# フォームからデータを取得
	area_form = input_area
	distance = input_distance
	# カラムデータを作成
	data = {'house_area': [area_form],
	        'distance': [distance]}
	# データフレームを作成
	df_form = pd.DataFrame(data)

	# フォームから取得したデータから特徴量を抽出
	x_form = df_form[feature_cols]
	# 学習したモデルを用いて予想
	df_form['pred_rent_price'] = model.predict(x_form)
	# 予測された値を取り出す
	prediction = df_form.loc[0, 'pred_rent_price']

	result = {'model_ases': round(model_ases,2), 'model_ases_per': math.floor(model_ases*100),'err_range': math.floor(err_range), 'area_form': area_form, 'distance': distance, 'prediction' : math.floor(prediction)}
	return result

# ファイル形式の判定
def path_flag(filename):
	# ドットで分割して最後の要素が '.csv' で終わっているかどうかを確認
	if filename.lower().endswith('.csv'):
		file_flag = 1
	else:
		file_flag = 0
	return file_flag