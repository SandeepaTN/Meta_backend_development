from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import Order, OrderItem, MenuItem, Cart,Category
from .serializers import CategorySerializer, MenuItemSerializer, UserSerializer, ManagerUserSerializer,CartSerializer,OrderSerializer,OrderItemSerializer,SingleOrderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView,DestroyAPIView 
from rest_framework.response import Response
from .permissions import IsManagerOrReadOnly, IsManager
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
class CategoryView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = [IsManagerOrReadOnly]
    
  

class SingleCategoryView(RetrieveUpdateDestroyAPIView):
    #lookup_field = "id"  # Set lookup_field to 'id'
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrReadOnly]
    def get_queryset(self):
        id=self.kwargs["pk"]
        return Category.objects.filter(id=id)
    


class MenuItemView(ListCreateAPIView):
    queryset=MenuItem.objects.select_related("category").all()
    serializer_class=MenuItemSerializer
    permission_classes = [IsManagerOrReadOnly]
    ordering_fields=["price","title"]
    search_fields=["title"]
    
    

class SingleItemView(RetrieveUpdateDestroyAPIView):
    serializer_class=MenuItemSerializer
    permission_classes=[IsManagerOrReadOnly]
    def get_queryset(self):
        id=self.kwargs["pk"]
        return MenuItem.objects.filter(id=id)
    

class ManagerView(ListCreateAPIView):
    permission_classes=[IsAdminUser]
    serializer_class = ManagerUserSerializer

    def get_queryset(self):
        try:
            managers_group=Group.objects.get(name="Manager")
            return managers_group.user_set.all()
        except Group.DoesNotExist:
            return User.objects.none()
        
    def create(self, request, *args, **kwargs):
       serializer=ManagerUserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       username=serializer.validated_data["username"]
       try:
           user=User.objects.get(username=username)
           managers_group = Group.objects.get(name="Manager")
           managers_group.user_set.add(user)
           return Response(
               {"message": f"User '{username}' added to the Manager group."},
               status=status.HTTP_201_CREATED,
           )
       except User.DoesNotExist:
           return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)



class SingleManagerView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ManagerUserSerializer
    def get_queryset(self):
        id=self.kwargs["pk"]
        try:
            managers_group = Group.objects.get(name="Manager")
            return managers_group.user_set.filter(id=id)
        except Group.DoesNotExist:
            return User.objects.none()    
    def destroy(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        try:
           user = User.objects.get(id=id)
           managers_group = Group.objects.get(name="Manager")
           managers_group.user_set.remove(user)
           return Response(
               {"message": f"User '{id}' deleted the Manager group."},
               
           )
        except User.DoesNotExist:
           return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class DeliveryCrewview(ListCreateAPIView):
    
    permission_classes = [IsManager]
    serializer_class = ManagerUserSerializer

    def get_queryset(self):
        try:
            delivey_group = Group.objects.get(name="DeliveryCrew")
            return delivey_group.user_set.all()
        except Group.DoesNotExist:
            return User.objects.none()

    def create(self, request, *args, **kwargs):
       serializer = ManagerUserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       username = serializer.validated_data["username"]
       try:
           user = User.objects.get(username=username)
           delivey_group = Group.objects.get(name="DeliveryCrew")
           delivey_group.user_set.add(user)
           return Response(
               {"message": f"User '{username}' added to the DeliveryCrew group."},
               status=status.HTTP_201_CREATED,
           )
       except User.DoesNotExist:
           return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class SingleDeliveryCrewView(RetrieveDestroyAPIView):
    permission_classes = [IsManager]
    serializer_class = ManagerUserSerializer

    def get_queryset(self):
        id = self.kwargs["pk"]
        try:
            delivey_group = Group.objects.get(name="DeliveryCrew")
            return delivey_group.user_set.filter(id=id)
        except Group.DoesNotExist:
            return User.objects.none()

    def destroy(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        try:
           user = User.objects.get(id=id)
           delivey_group = Group.objects.get(name="DeliveryCrew")
           delivey_group.user_set.remove(user)
           return Response(
               {"message": f"User '{id}' deleted the DeliveryCrew group."},

           )
        except User.DoesNotExist:
           return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class CartView(ListCreateAPIView,DestroyAPIView):
    
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]    
    def get_queryset(self):
        user=self.request.user
        return Cart.objects.filter(user=user)    
    def perform_create(self, serializer):
        user = self.request.user
        menuitem = serializer.validated_data.get("menuitem")

        if Cart.objects.filter(user=user, menuitem=menuitem).exists():
            raise ValidationError("This item is already in your cart. Please update the quantity instead.")

     
        serializer.save(user=user)
        
        
    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response({"message":"Cart Emptied"})
    
class OrderView(ListCreateAPIView):
    
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated,] 
    def get_queryset(self):
        if self.request.user.groups.filter(name="Manager").exists():
            return Order.objects.all()
        user=self.request.user
        if self.request.user.groups.filter(name="DeliveryCrew"):
      
            return Order.objects.filter (delivery_crew=user.id)
        return Order.objects.filter(user=user)
        
          
    
    def perform_create(self, serializer):
        user=self.request.user
        print(serializer.validated_data)
        cart_items=Cart.objects.filter(user=user)
        total=0
        ordered_items=[]
        for cart_item in cart_items:
            total+=cart_item.price
            ordered_items.append({
                "menuitem":cart_item.menuitem,
                "quantity":cart_item.quantity,
                "unitprice":cart_item.unit_price,
                "price":cart_item.price
            })
        if total==0:
            raise ValidationError("Cart is empty")
        order=serializer.save(user=user,total=total)
        for ordered_item in ordered_items:
            OrderItem.objects.create(
                order=order,
                menuitem=ordered_item["menuitem"],
                quantity=ordered_item["quantity"],
                unit_price=ordered_item["unitprice"],
                price=ordered_item["price"]
                
                
            )
            
        cart_items.delete()
        
        
class SingleOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = request.user

        # Manager access
        if user.groups.filter(name="Manager").exists():
            order = self.get_object(pk)
            serializer = SingleOrderSerializer(order)
            return Response(serializer.data)

        # DeliveryCrew access
        elif user.groups.filter(name="DeliveryCrew").exists():
            order = Order.objects.filter(id=pk, delivery_crew=user).first()
            if not order:
                return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SingleOrderSerializer(order)
            return Response(serializer.data)

        # Customer access
        else:
            order = Order.objects.filter(id=pk, user=user).first()
            if not order:
                return Response({"detail": "Order not found or does not belong to you."},
                                status=status.HTTP_404_NOT_FOUND)
            items = OrderItem.objects.filter(order=order)
            serializer = OrderItemSerializer(items, many=True)
            return Response(serializer.data)

    def patch(self, request, pk):
        user = request.user
        order = self.get_object(pk)

        # DeliveryCrew can only update the status
        if user.groups.filter(name="DeliveryCrew").exists():
            if order.delivery_crew != user:
                return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
            status_data = request.data.get("status")
            if status_data in [0, 1]:  # Ensure valid status values
                order.status = status_data
                order.save()
                return Response({"detail": "Order status updated."}, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)

        # Manager can update delivery crew and status
        elif user.groups.filter(name="Manager").exists():
            serializer = SingleOrderSerializer(
                order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, pk):
        user = request.user

        # Only Manager can delete orders
        if user.groups.filter(name="Manager").exists():
            order = self.get_object(pk)
            order.delete()
            return Response({"detail": "Order deleted."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
