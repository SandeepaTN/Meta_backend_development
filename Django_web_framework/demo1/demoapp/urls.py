from django.urls import path,re_path
from . import views

app_name='demoapp'      #application namespace
urlpatterns = [path('index/<int:id>', views.index, name='inde'), 
               path('home', views.home, name='index'),
               path('register/',views.showform, name='register'),
               #path('user/', views.getform, name='user'), 
               path('user/', views.Getform.as_view(), name='user'),  #classbased
               re_path(r'reg/([0-9]{2})',views.reg),
               path('applicants',view=views.applicants,name='applicants'),
               ]