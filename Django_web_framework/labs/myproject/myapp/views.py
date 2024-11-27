from django.shortcuts import render

# Create your views here.
from .forms import  BookingForm


def booking(request):
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,"bookings.html",context)