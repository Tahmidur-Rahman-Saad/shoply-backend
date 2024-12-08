from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def all_user(request):
    return HttpResponse("Hello World")

@api_view(['GET'])
def show_users(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({"message": "Show all users successfully",'users':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_user(request,pk):
    if request.method == 'GET':
        try:    
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response({"message": "Show the user successfully",'user':serializer.data}
                        ,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        try:
            data = request.data
            data['password'] = make_password(data.get('password')) 
            serializer = UserSerializer(data=data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Create Usersuccessfully!', 'user': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_user(request,pk):
    if request.method == 'PUT':
        try:    
            user = User.objects.get(pk = pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Update Usersuccessfully!', 'user': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request,pk):
    if request.method == 'DELETE':
        try:    
            user = User.objects.get(pk = pk)
            user.delete()
            return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Not Deleted!!!"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password :
            return Response({'error': 'Email and password are required.'}, 
                    status=status.HTTP_400_BAD_REQUEST)
        try:       
            user = User.objects.get(email=email)
            if check_password(password, user.password): 
                serializer = UserSerializer(user)
                return Response(
                    {'message': 'Login successful!', 'user': serializer.data}, 
                    status=status.HTTP_200_OK
                )
                
            else:
                return Response(
                    {'error': 'Invalid password.'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except:
            return Response({'error': 'User not found.'},status=status.HTTP_404_NOT_FOUND)