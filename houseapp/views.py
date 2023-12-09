from django.shortcuts import render

def index(request):
	params = {
		'title' : 'Table Of Contents',
	}
	return render(request, 'index.html', params)
