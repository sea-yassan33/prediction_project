from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('house/',views.house, name='house'),
	path('houselist/',views.houselist, name='houselist'),
]