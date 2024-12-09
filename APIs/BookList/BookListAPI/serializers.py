from rest_framework import serializers
from .models import Book





class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields='__all__'