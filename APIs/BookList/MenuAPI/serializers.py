from rest_framework  import serializers
from .models import Menu,Category
from decimal import Decimal
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
import bleach  # to Sanitize HTML and JavaScript
# class MenuSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     name=serializers.CharField(max_length=255)

class CategorySerializers(serializers.ModelSerializer): 
    class Meta:
        model=Category
        fields="__all__"

# class MenuSerializer(serializers.ModelSerializer):
#     title=serializers.CharField(source='name')
#     total=serializers.SerializerMethodField(method_name='calculate_tax')
#     # category=CategorySerializers() #relationship serializers #method1
#     class Meta:
#         model=Menu
#         #fields="__all__"
#         depth=1  #method2
#         fields=['id','title','price','total','category']
        
#     def calculate_tax(self,product:Menu):
#         return product.price*1.1


# method1  category field as a hyperlink
# class MenuSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(source='name')
#     total = serializers.SerializerMethodField(method_name='calculate_tax')
#     category=serializers.HyperlinkedRelatedField(
#         queryset=Category.objects.all(),
#         view_name="category-detail"
#     )
#     class Meta:
#         model = Menu
#         # fields="__all__"
#         
#         fields = ['id', 'title', 'price', 'total', 'category']

#     def calculate_tax(self, product: Menu):
#         return product.price*1.1
    
    

# class MenuSerializer(serializers.HyperlinkedModelSerializer):
#     title = serializers.CharField(source='name')
#     total = serializers.SerializerMethodField(method_name='calculate_tax')
#     
#     category_id=serializers.IntegerField(write_only=True)

#     class Meta:
#         model = Menu
#         # fields="__all__"
        
#         fields = ['id', 'title', 'price', 'total', 'category','category_id']

#     def calculate_tax(self, product: Menu):
#         return product.price*1.1


class MenuSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(source='name')
    total = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializers(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    stock = serializers.IntegerField(source='inventory')
    # # Method 1: Conditions in the field
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, min_value=10)
    
    
        
    # class Meta:
    #     model = Menu
        
        
    #     fields = ['id', 'title', 'price','stock' ,'total', 'category', 'category_id']
    #     extra_kwargs = {  # Method 2: Using keyword arguments in the Meta class
    #         "price": {'min_value': 10},
    #         "stock": {"source": "inventory", 'min_value': 0},
    #         "title": {"source":"name",
    #             "validators": [
    #                 UniqueValidator(
    #                     queryset=Menu.objects.all()
    #                 )
    #             ]
    #         }
    #     }

    title = serializers.CharField(source='name')

    def validate(self, attrs):
        print(attrs)
        attrs['name'] = bleach.clean(attrs['name'])
        
        return super().validate(attrs)
    class Meta:
        model = Menu

        fields = ['id', 'title', 'price', 'stock','total', 'category', 'category_id']
        # validators=[
        #     UniqueTogetherValidator(
        #         queryset=Menu.objects.all(),
        #         fields=["title","price"]
        #     )
        # ]
        
        extra_kwargs = {  # Method 2: Using keyword arguments in the Meta class
            "price": {'min_value': 10},
            "stock": {"source": "inventory", 'min_value': 0},
            
        }

    def calculate_tax(self, product: Menu):
            return product.price*Decimal(1.1)
