from django.shortcuts import render

# Create your views here.

posts =[
	{
		'author': 'JK',
		'title': 'Random title',
		'content': 'Sample Text',
		'date_posted': 'today'
	},
	{
		'author': 'Someone',
		'title': 'Super title',
		'content': 'Content text',
		'date_posted': 'yesterday'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'app/app.html', context, {'title': 'Home'})
