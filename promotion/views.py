from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
import base64

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
@permission_classes([IsAuthenticated])
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
                'response': "Data not valid",
                'error': serializer.errors
            })
        # except Exception as e:
        #     # Handle unexpected errors
        #     return Response({
        #         'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         'response': "An unexpected error occurred",
        #         'error': str(e)
        #     })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def promotionUpdate(request, pk):

    try:
        profile_data = request.data
        promotion = Promotion.objects.get(pk=pk)
        
        if ('image' in profile_data and profile_data['image'] == None) and promotion.image != None:
                profile_data.pop('image')
                
        if 'image' in profile_data:
                fmt, img_str = str(profile_data['image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                profile_data['image'] = img_file
                

        serializer = PromotionSerializer(promotion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Promotion updated successfully",
                "data": serializer.data
            })
        else:
            
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not valid",
                'error': serializer.errors
            })

    except ObjectDoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'response': "Promotion not found"
        })
    except Exception as e:
        # Handle unexpected exceptions
        return Response({
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'response': "An unexpected error occurred",
            'error': str(e)
        })





@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
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
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def togglePromotionStatus(request, promotion_id):
    
    try:
        
        promotion = Promotion.objects.filter(id=promotion_id).first()
        if not promotion:
            return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'response': "Promotion not found"
            })
        promotion.is_active = not promotion.is_active
        promotion.save()

        if promotion.is_active:
            Promotion.objects.exclude(id=promotion_id).update(is_active=False)

        return Response({
            'code': status.HTTP_200_OK,
            'response': f"Promotion '{promotion.title}' toggled successfully",
            "data": {
                "id": promotion.id,
                "title": promotion.title,
                "is_active": promotion.is_active
            }
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'response': "An error occurred",
            'error': str(e)
        })
