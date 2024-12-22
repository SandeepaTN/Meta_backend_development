from django.shortcuts import render
from .models import MenuItem,Category
from .serializers import MenuItemSerializers,CategorySerializer
from rest_framework import generics
# Create your views here.


class CategoriesView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class MenuitemView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializers
    ordering_fields=["price",'inventory']
    search_fields=['category__title']
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
    
    