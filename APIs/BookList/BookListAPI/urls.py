from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('books',views.BookItemsView.as_view(),name="books"),
    path('books/<int:pk>',views.SingleBookView.as_view(),name='singlebook'),
    path("secret",views.secret),
    path("token-auth",obtain_auth_token),
    path("manager_secret",views.manager_view),
    path("throtle-check",views.throttle_check),
    path("throtle",views.throtle_custom),  
    path("manager",views.manager)
]


