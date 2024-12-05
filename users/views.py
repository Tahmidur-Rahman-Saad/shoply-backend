from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse

# Create your views here.
def all_user(request):
    return HttpResponse("Hello World")

@api_view(['GET'])
def show_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def retrieve_user(request,pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_user(request,pk):
    if request.method == 'PUT':
        user = User.objects.get(pk = pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request,pk):
    if request.method == 'DELETE':
        user = User.objects.get(pk = pk)
        user.delete()
        return Response({"message": "User Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

