from django.shortcuts import render

# Create your views here.

def home(request):
	#homepage view, returns homepage
	return render(request, 'app_web/homepage.html')



def workpage(request):
	#workpage view, returns a grid of card for projects/works done

	return render(request, 'app_web/workpage.html')

def aboutpage(request):
	#about page, return info about me

	return render(request, 'app_web/aboutpage.html')

def etc(request):
	#etc. page, to be decided later

	return render(request, 'app_web/etc.html')

def project_ecom(request):
	#project ecom under workpage

	return render(request, 'app_web/project_ecom.html')
