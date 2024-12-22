from rest_framework import serializers
from .models import MenuItem,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializers(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    category_id=serializers.IntegerField(write_only=True)
    
    class Meta:
        model=MenuItem
        fields="__all__"
        
        extra_kwargs={
            'price':{'min_value':2
                },
            'inventory':{'min_value':0
                
            }
        }
        
        
