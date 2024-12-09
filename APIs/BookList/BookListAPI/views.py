from django.shortcuts import render
from django.db import IntegrityError
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from  rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics     #for generic views
from .serializers import BookItemSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# @csrf_exempt
# def books(request):
#     if request.method == "GET":
#         books=Book.objects.all().values()
#         print(books)
#         return JsonResponse({"books":list(books)})
#     elif request.method == "POST":
#         title=request.POST.get("title")
#         author=request.POST.get('author')  
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory') 
#         print(title)
#         book=Book(title=title,author=author,price=price,inventory=inventory)  
#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({"error": "true,", "message": "required field missing"}, status= 400)
#         return JsonResponse(model_to_dict(book),status=201)


# @api_view(["GET","POST"])
# @csrf_exempt
# def books(request):
#     if request.method == "GET":
#         books = Book.objects.all().values()
#         print(books)
#         return Response({"books": list(books)},status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         title = request.data.get("title")
#         author = request.data.get('author')
#         price = request.data.get('price')
#         inventory = request.data.get('inventory')
#         print(title)
#         book = Book(title=title, author=author,
#                     price=price, inventory=inventory)
#         try:
#             book.save()
#         except IntegrityError:
#             return Response({"error": "true,", "message": "required field missing"}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(model_to_dict(book), status=status.HTTP_201_CREATED)


class BookItemsView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookItemSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields=['price','inventory']
    search_fields=['title','author']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    # def get_queryset(self):
    #         return Book.objects.all().filter(user=self.request.user)
    
class SingleBookView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookItemSerializer
    def get_permissions(self):
        permission_classes=[]
        if self.request.method!="GET":
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]

