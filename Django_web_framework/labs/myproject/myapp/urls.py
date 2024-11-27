from django.urls import path
from . import views

urlpatterns = [
    path('booking/',view=views.booking,name="booking")
]