from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from django.http import HttpResponse

# Create your views here.
def all_user(request):
    return HttpResponse("Hello World")

@api_view(['GET'])
def show_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def retrieve_products(request,pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
@api_view(['GET'])
def show_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_categories(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_categories(request,pk):
    if request.method == 'PUT':
        category = Category.objects.get(pk = pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



@api_view(['DELETE'])
def delete_categories(request,pk):
    if request.method == 'DELETE':
        category = Category.objects.get(pk = pk)
        category.delete()
        return Response({"message": "Categories deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['PUT'])
def update_products(request,pk):
    if request.method == 'PUT':
        product = Product.objects.get(pk = pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
def delete_products(request,pk):
    if request.method == 'DELETE':
        product = Product.objects.get(pk = pk)
        product.delete()
        return Response({"message": "products deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

