from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView, DeleteView
from django.views import View
from .models import Employee
from django.urls import reverse_lazy
# Create your views here.

class EmployeeCre(CreateView):
    model=Employee
    fields="__all__"
    success_url = reverse_lazy('generic_views:success')

class Successs(TemplateView):
    template_name='success.html'

class EmployoeeList(ListView):
    model=Employee
    fields="__all__"
    success_url = reverse_lazy('generic_views:success')


class EmployeeDetail(DetailView):
    model=Employee
    fields="__all__"


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy('generic_views:success')


class EmployeeDelete(DeleteView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy('generic_views:success')
