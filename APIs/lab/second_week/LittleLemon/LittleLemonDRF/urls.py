from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuitemView.as_view()),
     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category', views.CategoriesView.as_view()),
]