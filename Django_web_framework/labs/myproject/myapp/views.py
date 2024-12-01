from django.shortcuts import render

# Create your views here.
from .forms import  BookingForm
from .models import Menu


def booking(request):
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,"bookings.html",context)





def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day.",'name':'sandEepa'}
    return render(request, 'about.html',about_content)

def menu(request):
    menu_items=Menu.objects.all()
    menu_dict={"menu":menu_items}
    return render(request,'menu.html',menu_dict)

