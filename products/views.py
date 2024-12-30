from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from django.http import HttpResponse


@api_view(['GET'])
def show_products(request):
    if request.method == 'GET':
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response({"message": "Shows all product list successfully",'Products':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def retrieve_products(request,pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response({"message": "Shows product successfully",'Product':serializer.data}
                        , status=status.HTTP_200_OK)
        except: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def show_categories(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({"message": "Shows all categories successfully",'Product':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        try:
            serializer = ProductSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Product Created successfully",'Product':serializer.data},
                                status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def create_categories(request):
    if request.method == 'POST':
        try:
            serializer = CategorySerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message": "Product categories Created successfully",'Categories':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def update_categories(request,pk):
    if request.method == 'PUT':
        try:
            category = Category.objects.get(pk = pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Update categories successfully",'Categories':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_categories(request,pk):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(pk = pk)
            category.delete()
            return Response({"message": "Categories deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Categories not deleted!!!."}, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['PUT'])
def update_products(request,pk):
    if request.method == 'PUT':
        try:
            product = Product.objects.get(pk = pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Update products successfully",'Products':serializer.data},
                                 status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_products(request,pk):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk = pk)
            product.delete()
            return Response({"message": "products deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Products not deleted!!!."}, status=status.HTTP_400_BAD_REQUEST)

