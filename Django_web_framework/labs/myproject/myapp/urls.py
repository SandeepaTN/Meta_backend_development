from django.urls import path
from . import views
app_name='myapp'
urlpatterns = [
    path('booking/',view=views.booking,name="booking"),
    path('about/',view=views.about,name='about'),
    path('menu/',view=views.menu,name='menu'),
    
]