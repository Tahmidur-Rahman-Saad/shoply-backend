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
def show_promotions(request):
    if request.method == 'GET':
        try:
            promotions = Promotion.objects.all()
            serializer = PromotionSerializer(promotions, many=True)
            return Response({"message": "Shows all the promotions list successfully",'Promotions':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_promotion(request,pk):
    if request.method == 'GET':
        try:
            promotion = Promotion.objects.get(pk=pk)
            serializer = PromotionSerializer(promotion)
            return Response({"message": "Show the specific promotion successfully",'Promotion':serializer.data}
                        , status=status.HTTP_200_OK)
        except: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_promotion(request):
    if request.method == 'POST':
        try:
            serializer = PromotionSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Promotion Created successfully",'Promotion':serializer.data},
                                status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_promotion(request,pk):
    if request.method == 'PATCH':
        try:
            promotion = Promotion.objects.get(pk = pk)
            serializer = PromotionSerializer(promotion, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Update the promotion successfully",'Promotion':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_promotion(request,pk):
    if request.method == 'DELETE':
        try:
            promotion = Promotion.objects.get(pk = pk)
            promotion.delete()
            return Response({"message": "Selected promotion deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Promotion does not deleted!!!."}, status=status.HTTP_400_BAD_REQUEST)
    

