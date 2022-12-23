from django.shortcuts import render

# Create your views here.

def home(request):
	#homepage view, returns homepage
	return render(request, 'app_web/homepage.html')