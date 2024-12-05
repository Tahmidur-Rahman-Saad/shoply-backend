from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart,Order,CartItems
from .serializers import CartSerializer, OrderSerializer,CartItemsSerializer

@api_view(['GET'])
def show_orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    
    
@api_view(['GET'])
def retrieve_order(request,pk):
    if request.method == 'GET':
        orders = Order.objects.get(pk=pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)
 
@api_view(['GET'])
def retrieve_cartitem(request,pk):
    if request.method == 'GET':
        cartitem = CartItems.objects.get(pk=pk)
        serializer = CartItemsSerializer(cartitem)
        return Response(serializer.data)

@api_view(['POST'])
def create_cart(request):
    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_to_cartitems(request,pk):
    if request.method == 'POST':
        data = request.data 
        data['cart_id'] = pk
        serializer = CartItemsSerializer(data=data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_order(request,pk):
    if request.method == 'POST':
        data = request.data 
        data['cart_id'] = pk
        serializer = OrderSerializer(data=data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_cartitem(request, pk):
    if request.method == 'PUT':
        cartitem = CartItems.objects.get(pk=pk)
        serializer = CartItemsSerializer(cartitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_order(request, pk):
    if request.method == 'PUT':
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_cartitem(request, pk):
    if request.method == 'DELETE':
        cartitem = CartItems.objects.get(pk=pk)
        cartitem.delete()
        return Response({"message": "Cart Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)