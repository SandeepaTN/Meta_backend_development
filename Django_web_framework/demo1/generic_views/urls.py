from django.urls import path
from . import views
app_name='generic_views'
urlpatterns=[
    path("create/",view=views.EmployeeCre.as_view(),name="EmployeeCreate"),
    path('success/', view=views.Successs.as_view(), name='success'),
    path("list/",views.EmployoeeList.as_view(),name="list"),
    path("details/<int:pk>",views.EmployeeDetail.as_view(),name="details"),
    path("update/<int:pk>",views.EmployeeUpdate.as_view(),name="update"),
    path("delete/<int:pk>",views.EmployeeDelete.as_view(),name="delete")
]