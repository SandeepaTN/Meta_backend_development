from rest_framework import serializers
from .models import Order, OrderItem, MenuItem, Cart, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        

class MenuItemSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    category_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=MenuItem 
        fields = ["title", "price", "featured","category","category_id"]
    def get_category(self,obj):
        return obj.category.title if obj.category else None
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","groups"]

class ManagerUserSerializer(serializers.Serializer):
    username=serializers.CharField()
    id=serializers.IntegerField(read_only=True)
    
    
class CartSerializer(serializers.ModelSerializer):
    unitprice=serializers.SerializerMethodField()
    quantity=serializers.IntegerField()
    price=serializers.SerializerMethodField()
    
    class Meta:
        model=Cart
        fields=["menuitem","quantity","unitprice","user","price"]
        extra_kwargs={
            "user":{
                "read_only":True
            }
        }
        
    def get_unitprice(self,obj):
        return obj.menuitem.price if obj.menuitem else None
    
    def get_price(self,obj):
        return obj.unit_price*obj.quantity
    
    
    def create(self, validated_data):
        menuitem=validated_data.get("menuitem")
        quantity = validated_data.get("quantity")
        validated_data["unit_price"]=menuitem.price if menuitem else None
        validated_data["price"]=quantity*menuitem.price
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        menuitem = validated_data.get("menuitem")
        quantity = validated_data.get("quantity")
        validated_data["unit_price"] = menuitem.price if menuitem else None
        validated_data["price"] = quantity*menuitem.price
        return super().update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    class Meta:
        
        model=Order
        fields=["id","status","total","date","user","delivery_crew"]
        extra_kwargs={
            "user":{
                "read_only":True
            },
            "delivery_crew":{
                "read_only": True
            }
        }
        
        
class SingleOrderSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "total", "date", "user", "delivery_crew"]
        extra_kwargs = {
            "user": {  # Writable and optional
                "required": False,  # Not mandatory
            },
            "delivery_crew": {  # Writable and optional
                "required": False,  # Not mandatory
                "allow_null": True,  # Allow null values
            },
        }


class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=OrderItem
        fields=["id","quantity","unit_price","order","menuitem","price"]
        
        