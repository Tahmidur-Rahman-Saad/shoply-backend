from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes

# Create your views here.


@api_view(['GET'])
def promotions(request):
    if request.method == 'GET':
        try:
            promotions = Promotion.objects.all()
            serializer = PromotionSerializer(promotions, many=True)
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

@api_view(['GET'])
def promotionDetails(request,pk):
    if request.method == 'GET':
        try:
            promotion = Promotion.objects.get(pk=pk)
            serializer = PromotionSerializer(promotion)
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



@api_view(['POST'])
@permission_classes([IsAdminUser])
def promotionCreate(request):
    if request.method == 'POST':
        try:
            serializer = PromotionSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Personal Information Updated successfully",
                    "data": serializer.data
                })
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })




@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def promotionUpdate(request,pk):
    if request.method == 'PATCH':
        try:
            promotion = Promotion.objects.get(pk = pk)
            serializer = PromotionSerializer(promotion, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Personal Information Updated successfully",
                    "data": serializer.data
                })
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def promotionDelete(request,pk):
    try:
        if Promotion.objects.filter(id=pk).exists():
            instance = Promotion.objects.get(id=pk)
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
    
