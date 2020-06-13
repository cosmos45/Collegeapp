from . import views
from django.urls import path

app_name = 'resume'

urlpatterns = [
    path('resume/', views.Rbase, name='resume'),
    path('temp1/', views.temp1, name='temp1'),
    path('resume_with_image/', views.resumewi, name='resume_with_image'),



]
