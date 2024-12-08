from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart,Order,CartItems
from .serializers import CartSerializer, OrderSerializer,CartItemsSerializer

@api_view(['GET'])
def show_orders(request):
    if request.method == 'GET':
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({"message": "Show all order list successfully",'Orders':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    
@api_view(['GET'])
def retrieve_order(request,pk):
    if request.method == 'GET':
        try:
            orders = Order.objects.get(pk=pk)
            serializer = OrderSerializer(orders)
            return Response({"message": "Show the order successfully",'orders':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['GET'])
def retrieve_cartitem(request,pk):
    if request.method == 'GET':
        try:
            cartitem = CartItems.objects.get(pk=pk)
            serializer = CartItemsSerializer(cartitem)
            return Response({"message": "Show the cart item successfully",'order':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_cart(request):
    if request.method == 'POST':
        try:
            data = request.data 
            serializer = CartSerializer(data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Create cart successfully",'Cart':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def add_to_cartitems(request,pk):
    if request.method == 'POST':
        try:
            data = request.data 
            data['cart_id'] = pk
            serializer = CartItemsSerializer(data=data)
        
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Create cart item successfully",'Cart Item':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_order(request,pk):
    if request.method == 'POST':
        try:    
            data = request.data 
            data['cart_id'] = pk
            serializer = OrderSerializer(data=data)
        
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Order corfirmed!!!",'Order':serializer.data}
                                , status=status.HTTP_201_CREATED)
        
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_cartitem(request, pk):
    if request.method == 'PUT':
        try:
            cartitem = CartItems.objects.get(pk=pk)
            serializer = CartItemsSerializer(cartitem, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Update Cart item successfully!!!",'cart item':serializer.data}
                                , status=status.HTTP_200_OK)
            
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_order(request, pk):
    if request.method == 'PUT':
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Update Order successfully!!!",'cart item':serializer.data}
                                , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_cartitem(request, pk):
    if request.method == 'DELETE':
        try:
            cartitem = CartItems.objects.get(pk=pk)
            cartitem.delete()
            return Response({"message": "Cart Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Not Deleted!!!"}, status=status.HTTP_400_BAD_REQUEST)