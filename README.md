# プロジェクト名：　prediction_project

# 概要
- 様々なモデルを使用し予測アプリを作成

# Pythonの導入

# Djangoの導入
- プロジェクト作成
```
django-admin startproject [プロジェクト名]
```

- ローカルアクセス
```
cd [プロジェクト名]
python manage.py runserver
```

- urlアクセス
```
http://localhost:8000/
http://localhost:8000/house/
```

# アプリの作成
- アプリ作成
```
[terminal]
python manage.py startapp [アプリケーション名]
```

- プロジェクト内に作成したアプリを登録
```
prediction_project > settings.py

INSTALLED_APPS = [
    ・・・
	'houseapp',
]
```

- 作成したアプリ内でurls.pyを作成
```
houseapp > urls.py(新規作成)
```

- プロジェクト内のurls.pyの設定変更
```
prediction_project > urls.py

from django.urls import path, include //includeを追加

path('house/', include('houseapp.urls')), //追加
```

# MVC作成手順
### view テンプレートを作成
- テンプレートファイルの作成
- htmlファイルの作成
  
### control views.pyの修正
- htmlファイルに渡すデータを作成

### model

# フォームの作成
- app内にforms.pyを作成
- imageやcsvなどのファイルを送る際は以下の設定を行う
```
[setting.py]
import os #追加

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```
[urls.py(プロジェクト内)]
from django.conf import settings #追加
from django.conf.urls.static import static #追加

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```
[xxx.html]
<form method=“POST” enctype=“multipart/form-data”>
    {% csrf_token %}
    <input type=“file” name=“testfile”>
    <button type=“submit”>アップロード</button>
</form>
```