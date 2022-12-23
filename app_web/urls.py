from django.urls import path
from . import views 

#django app: app_web containing frontend templates

app_name = 'app_web'

urlpatterns = [
				path('', views.home, name='homepage')
				]