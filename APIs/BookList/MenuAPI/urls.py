from django.urls import path
from . import views

urlpatterns=[
    path("menu",views.menu,name="menu"),
    path("menu/<int:id>",views.single_item,name="single_item"),
    path("category/<int:pk>",views.category_detail,name="category-detail"),
    path("category",views.category,name="category")
]