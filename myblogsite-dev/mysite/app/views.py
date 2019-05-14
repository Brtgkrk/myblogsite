from django.shortcuts import render
from django.http import HttpResponse #temporary

# Create your views here.

posts =[
	{
		'author': 'Jakub Krok',
		'title': 'Jak stworzyć interaktywną strone w Django?',
		'content': 'Chciałeś kiedyś stworzyć własną aplikację internetową ale nie wiedziałeś jak? Znakomicie! ten poradnik jest właśnie dla ciebie',
		'date_posted': '10.05.2019'
	},
	{
		'author': 'Nikodem Sroga',
		'title': 'Modelowanie w aplikacji Blender',
		'content': 'Kompleksowy poradnik modelowania oraz texturowania w darmowej aplikacji Blender',
		'date_posted': '9.05.2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'app/app.html', context, {'title': 'BlogHome'})

def about(request):
	return render(request, 'app/about.html', {'title': 'AboutUs'})
