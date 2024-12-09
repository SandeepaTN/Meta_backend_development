from django.shortcuts import render
from .models import Menu,Category
from rest_framework.response  import Response
from  .serializers import MenuSerializer,CategorySerializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator,    EmptyPage


from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer  
from rest_framework_csv.renderers import CSVRenderer

@api_view(["GET","POST"])
#@renderer_classes([CSVRenderer])
def menu(request):
    if request.method=="GET":
        # items=Menu.objects.all()
        items=Menu.objects.select_related('category').all()  #to minimize sql calls in relationship seria
        # print(items)
        category_name=request.query_params.get("category")
        to_price=request.query_params.get("to_price")
        search=request.query_params.get("search")
        ordering=request.query_params.get("ordering")
        
        perpage=request.query_params.get("perpage",default=5)
        page=request.query_params.get('page',default=1)
        
        if category_name:
            items=items.filter(category__title=category_name)
        if to_price:
            items=items.filter(price__lte=to_price)
        if search:
           items=items.filter(name__startswith=search)
           #items = items.filter(name__contains=search)
        if ordering: # for descending just http://127.0.0.1:8000/menu-api/menu?ordering=-price (use -price)
            #items = items.order_by(ordering)
            ordering_fields=ordering.split(",")
            items=items.order_by(*ordering_fields)
            
        paginator=Paginator(items,per_page=perpage)
        try:                                    #to handle empty page error
            items=paginator.page(number=page)
        except EmptyPage:
            items=[]    
        
        serialized_items=MenuSerializer(items,many=True,context={"request":request})  # context for hyperlink related
        return Response(serialized_items.data)
    if request.method=="POST":
        serialized_item=MenuSerializer(data=request.data)
        print(serialized_item)
        serialized_item.is_valid(raise_exception=True)
        print(serialized_item._validated_data)
        serialized_item.save()
        return Response(serialized_item.data,status.HTTP_201_CREATED)


@api_view(["GET"])
def single_item(request,id):
    # item=Menu.objects.get(pk=id)
    item=get_object_or_404(Menu,pk=id)
    serialized_item=MenuSerializer(item)
    return Response(serialized_item.data)
    
   
   
@api_view()

def category_detail(request,pk):
    category=get_object_or_404(Category,pk=pk)
    serialized_category=CategorySerializers(category)
    return Response(serialized_category.data)


@api_view()
@renderer_classes([TemplateHTMLRenderer])
def category(request,):
    category = Category.objects.all()
    serialized_category = CategorySerializers(category,many=True)
    return Response({"categories":serialized_category.data},template_name='category.html')
    
    

