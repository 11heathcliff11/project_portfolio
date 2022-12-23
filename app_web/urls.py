from django.urls import path
from . import views 

#django app: app_web containing frontend templates

app_name = 'app_web'

urlpatterns = [
				path('', views.home, name='homepage'),
				path('workpage', views.workpage, name='workpage'),
				path('aboutpage', views.aboutpage, name='aboutpage'),
				path('etc', views.etc, name='etc'),


				#projects under work
				path('workpage/project_ecom', views.project_ecom, name='project_ecom'),
				]