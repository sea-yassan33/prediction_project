from django.shortcuts import render

def index(request):
	params = {
		'title' : 'hello Django',
	}
	return render(request, 'index.html', params)
