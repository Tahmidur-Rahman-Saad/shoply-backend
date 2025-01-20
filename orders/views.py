from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart,Order,CartItems
from .serializers import CartSerializer, OrderSerializer,CartItemsSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orders(request):
    if request.method == 'GET':
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            # return Response({"message": "Show all order list successfully",'Orders':serializer.data}
            #             , status=status.HTTP_200_OK)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'data': serializer.data
            })
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orderDetails(request,pk):
    if request.method == 'GET':
        try:
            orders = Order.objects.get(pk=pk)
            serializer = OrderSerializer(orders)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'data': serializer.data
            })
            # return Response({"message": "Show the order successfully",'orders':serializer.data}
            #             , status=status.HTTP_200_OK)
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


 
@api_view(['GET'])
def cartItemDetails(request,pk):
    if request.method == 'GET':
        try:
            cartitem = CartItems.objects.get(pk=pk)
            serializer = CartItemsSerializer(cartitem)
            product_details = cartitem.product_id
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'data': serializer.data,
                'product': {
                    'name': product_details.name,
                    'price': product_details.price,
                    'product details': product_details.details
                }
            })
            # return Response({"message": "Show the cart item successfully",'order':serializer.data}
            #             , status=status.HTTP_200_OK)
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cartCreate(request):
    if request.method == 'POST':
        try:
            data = request.data 
            serializer = CartSerializer(data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Cart Created Successfully",
                    "data": serializer.data
                })

        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cartItemAdd(request,pk):
    if request.method == 'POST':
        try:
            data = request.data 
            data['cart_id'] = pk
            serializer = CartItemsSerializer(data=data)
        
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Cart Item Created Successfully",
                    "data": serializer.data
                })

        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def orderConfirm(request,pk):
    if request.method == 'POST':
        try:    
            data = request.data 
            data['cart_id'] = pk
            data['confirmation'] = True
            serializer = OrderSerializer(data=data)
        
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'code': status.HTTP_201_CREATED,
                    'response': "Order Confirmed Successfully",
                    "data": serializer.data
                })
                # return Response({"message": "Order corfirmed!!!",'Order':serializer.data}
                #                 , status=status.HTTP_201_CREATED)
        
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
          


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def orderCancel(request,pk):
    if request.method == 'POST':
        try:    
            data = request.data 
            data['cart_id'] = pk
            data['confirmation'] = False
            serializer = OrderSerializer(data=data)
        
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'code': status.HTTP_201_CREATED,
                    'response': "Order Cancelled Successfully",
                    "data": serializer.data
                })
                # return Response({"message": "Order cancelled!!!",'Order':serializer.data}
                #                 , status=status.HTTP_201_CREATED)
        
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })




@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def cartItemUpdate(request, pk):
    if request.method == 'PATCH':
        try:
            cartitem = CartItems.objects.get(pk=pk)
            serializer = CartItemsSerializer(cartitem, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Cart Item Updated Successfully",
                    "data": serializer.data
                })
            
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })




@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def orderUpdate(request, pk):
    if request.method == 'PATCH':
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Order Updated Successfully",
                    "data": serializer.data
                })

        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
    



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cartItemDelete(request, pk):
    if request.method == 'DELETE':
        try:
            if CartItems.objects.filter(id=pk).exists():
                instance = CartItems.objects.get(pk=pk)
                instance.delete()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Deleted successfully.'
                })
            
            else:
                return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'Record not found.'
            })

        except Exception as e:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': str(e)
            }) 
  

#show all the confirmed orders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ordersConfirmList(request):
    try:
        orders = Order.objects.filter(confirmation = True)
        serializer = OrderSerializer(orders, many=True)
        return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Shows all confirmed order list successfully",
                    "data": serializer.data
                })

        
    except:
        return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })



#show all the cancel orders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ordersCancelList(request):
    try:
        orders = Order.objects.filter(confirmation = False)
        serializer = OrderSerializer(orders, many=True)
        return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Shows all Cancelled order list successfully",
                    "data": serializer.data
                })

    except:
        return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })

