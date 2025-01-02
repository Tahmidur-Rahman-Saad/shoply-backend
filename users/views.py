from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,AdminInfo
from django.contrib.auth.models import User
from .serializers import CustomerSerializer,AdminInfoSerializer, UserReadSerializer,UserSerializer,UserLoginSerializer
from django.contrib.auth.hashers import make_password,check_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes


#shows all the customers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_customers(request):
    if request.method == 'GET':
        try:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response({"message": "Show all users successfully",'Customers':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#shows all the admins & their informations
@api_view(['GET'])
@permission_classes([IsAdminUser])
def show_admininfos(request):
    if request.method == 'GET':
        try:
            admininfos = AdminInfo.objects.all()
            serializer = AdminInfoSerializer(admininfos, many=True)
            return Response({"message": "Show all admins successfully",'Admins':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#get all of the information for a selected customer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_customer(request,pk):
    if request.method == 'GET':
        try:    
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response({"message": "Show the user successfully",'Customer':serializer.data}
                        ,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get all of the information for a selected Admin
@api_view(['GET'])
@permission_classes([IsAdminUser])
def retrieve_admininfo(request,pk):
    if request.method == 'GET':
        try:    
            admininfo = AdminInfo.objects.get(pk=pk)
            serializer = AdminInfoSerializer(admininfo)
            return Response({"message": "Show the Admin successfully",'Admin':serializer.data}
                        ,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

#create a new customer with given user
@api_view(['POST'])
def create_customer(request):
    if request.method == 'POST':
        try:
            data = request.data
            serializer = CustomerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Create Usersuccessfully!', 'Customer': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

#create a new Admin with given user
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_admininfo(request):
    if request.method == 'POST':
        try:
            data = request.data
            serializer = AdminInfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Create Admin successfully!', 'Admin': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Update the selected customer
@api_view(['PATCH'])
def update_customer(request,pk):
    if request.method == 'PATCH':
        try:    
            customer = Customer.objects.get(pk = pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Update Usersuccessfully!', 'Customer': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Update the selected admin
@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_admininfo(request,pk):
    if request.method == 'PATCH':
        try:    
            admininfo = AdminInfo.objects.get(pk = pk)
            serializer = AdminInfoSerializer(admininfo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Update User successfully!', 'Admin': serializer.data}, 
                                status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)


#delete the selected customer
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_customer(request,pk):
    if request.method == 'DELETE':
        try:    
            customer = Customer.objects.get(pk = pk)
            user = customer.user

            customer.delete()
            user.delete()

            return Response({"message": "Customer deleted successfully."},
                            status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Not Deleted!!!"}, 
                            status=status.HTTP_400_BAD_REQUEST)


#delete the selected admin
@api_view(['DELETE'])
def delete_admininfo(request,pk):
    if request.method == 'DELETE':
        try:    
            admininfo = AdminInfo.objects.get(pk = pk)
            user = admininfo.user
            admininfo.delete()
            user.delete()
            return Response({"message": "Admin deleted successfully."},
                            status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Not Deleted!!!"}, 
                            status=status.HTTP_400_BAD_REQUEST)


#login with email
# @api_view(['POST'])
# def login_user(request):
#     if request.method == 'POST':
#         loginSerializer = UserLoginSerializer(data = request.data)
#         print("firstline")
#         if loginSerializer.is_valid():     
#             print("inside serializer")
#             email = loginSerializer.validated_data.get('email')
#             password = loginSerializer.validated_data.get('password')
#             print("inside serializer 2")

#             if not email or not password :
#                 return Response({'error': 'email and Password are required.'}, 
#                     status=status.HTTP_400_BAD_REQUEST)
            
#             user_instance = User.objects.get(email=email)
#             print("after user fetch")
#             if password == user_instance.password: 
#                 print("inside password")
#                 refresh = RefreshToken.for_user(user_instance)
#                 tokens = {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                     } 
                       
#                 serializer1 = UserReadSerializer(user_instance)
                
#                 return Response(
#                     {'message': 'Login successful!',
#                       'tokens': tokens,
#                       'customer': serializer1.data}, 
#                     status=status.HTTP_200_OK
#                 )             
#             else:
#                 return Response(
#                     {'error': 'Invalid password.'}, 
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )

#         return Response({'error': 'customer not found.'},status=status.HTTP_404_NOT_FOUND)


#Customer & user is created at the same time
@api_view(['POST'])
def create_user_customer(request):
    try:
        #after using try except, must be give response 
        data = request.data
        data1 ={
            'username': data['username'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email':data['email'],
            'password': data['password'],
            'is_staff' : False
        }

        data2 = {
            'phone' :data['phone']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = CustomerSerializer(data=data2)


        if serializer1.is_valid() and serializer2.is_valid():

            print("inside serializer1")
            user_serializer = serializer1.save()
            user = User.objects.get(username=data1['username'])
            serializer2.save(user = user)

            return Response({'message': 'Create Customer successfully!'}, 
                status=status.HTTP_201_CREATED)
            
    except:
       return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)



#AdminInfo & user is created at the same time
@api_view(['POST'])
def create_user_admininfo(request):
    try:
        #after using try except, must be give response 
        data = request.data
        data1 ={
            'username': data['username'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': data['password'],
            
        }

        data2 = {
            'phone' :data['phone'],
            'nid' : data['nid']
            # 'image' : data['image']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = AdminInfoSerializer(data=data2)


        if serializer1.is_valid() and serializer2.is_valid():

            print("inside serializer1")
            user_serializer = serializer1.save()
            user = User.objects.get(username=data1['username'])
            user.is_staff = True
            user.save()
            serializer2.save(user = user)

            return Response({'message': 'Create Admin successfully!'}, 
                status=status.HTTP_201_CREATED)
            
    except:
       return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)






#login data with username 
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        loginSerializer = UserLoginSerializer(data = request.data)
        print("firstline")
        if loginSerializer.is_valid():     
            print("inside serializer")
            username = loginSerializer.validated_data.get('username')
            password = loginSerializer.validated_data.get('password')
            print("inside serializer 2")

            if not username or not password :
                return Response({'error': 'Username and Password are required.'}, 
                    status=status.HTTP_400_BAD_REQUEST)
            
            user_instance = User.objects.get(username=username)
            print("after user fetch")
            if password == user_instance.password: 
                print("inside password")
                refresh = RefreshToken.for_user(user_instance)
                tokens = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    } 
                       
                serializer1 = UserReadSerializer(user_instance)
                
                return Response(
                    {'message': 'Login successful!',
                      'tokens': tokens,
                      'customer': serializer1.data}, 
                    status=status.HTTP_200_OK
                )             
            else:
                return Response(
                    {'error': 'Invalid password.'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )

        return Response({'error': 'customer not found.'},status=status.HTTP_404_NOT_FOUND)



#reset password for all types of user
@api_view(['PATCH'])
def reset_password(request):
    username = request.data.get('username')
    new_password = request.data.get('new_password')
    confirm_new_password = request.data.get('confirm_new_password')
    try:
        user = User.objects.get(username=username)
        if new_password != confirm_new_password:
            return Response({'message': 'Password does not match.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if new_password == user.password:
            return Response({'message': 'Please change the password. Matched with previous one'},
                            status=status.HTTP_400_BAD_REQUEST)
        user.password = new_password
        user.save()
        return Response({'message': 'Password has been reset successfully.'},
                        status=status.HTTP_200_OK)

    except:
        return Response ({'error': 'User with this username does not exist.'}, status=status.HTTP_404_NOT_FOUND)
