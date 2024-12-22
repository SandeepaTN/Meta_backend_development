from django.urls import path
from . import views

urlpatterns = [
    path("category",views.CategoryView.as_view(),name="category"),
    path("category/<int:pk>",views.SingleCategoryView.as_view(),name="category-detail"),
    path("menu-items",views.MenuItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleItemView.as_view(),name="menu-item-detail"),  
    path("groups/manager/users",views.ManagerView.as_view(),name="managers"),
    path("groups/manager/users/<int:pk>", views.SingleManagerView.as_view(), name="managers-detail"),
    path("groups/delivery-crew/users",views.DeliveryCrewview.as_view(),name="delivery-crew"),
    path("groups/delivery-crew/users/<int:pk>",views.SingleDeliveryCrewView.as_view(), name="delivery-crew-detail"),
    path("cart/menu-items",views.CartView.as_view(),name="cart"),
    path("orders",views.OrderView.as_view(),name="orders"),
    path("orders/<int:pk>",views.SingleOrderView.as_view(),name="single-detail"),
] 