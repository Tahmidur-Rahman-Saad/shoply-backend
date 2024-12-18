from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,AdminInfo
from .serializers import CustomerSerializer,AdminInfoSerializer


# Create your views here.
def all_user(request):
    return HttpResponse("Hello World")


#shows all the customers
@api_view(['GET'])
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
def show_admininfos(request):
    if request.method == 'GET':
        try:
            admininfos = AdminInfo.objects.all()
            serializer = AdminInfoSerializer(admininfos, many=True)
            return Response({"message": "Show all admins successfully",'Admins':serializer.data}
                        , status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_customer(request,pk):
    if request.method == 'GET':
        try:    
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response({"message": "Show the user successfully",'Customer':serializer.data}
                        ,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

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



@api_view(['PUT'])
def update_customer(request,pk):
    if request.method == 'PUT':
        try:    
            customer = Customer.objects.get(pk = pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Update Usersuccessfully!', 'Customer': serializer.data}, 
                    status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_customer(request,pk):
    if request.method == 'DELETE':
        try:    
            customer = Customer.objects.get(pk = pk)
            customer.delete()
            return Response({"message": "Customer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Not Deleted!!!"}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def login_customer(request):
#     if request.method == 'POST':
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password :
#             return Response({'error': 'Email and password are required.'}, 
#                     status=status.HTTP_400_BAD_REQUEST)
#         try:       
#             customer = Customer.objects.get(email=email)
#             if check_password(password, customer.password): 

#                 serializer = CustomerSerializer(customer)
#                 return Response(
#                     {'message': 'Login successful!',
#                       'customer': serializer.data}, 
#                     status=status.HTTP_200_OK
#                 )
                
#             else:
#                 return Response(
#                     {'error': 'Invalid password.'}, 
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )
#         except:
#             return Response({'error': 'customer not found.'},status=status.HTTP_404_NOT_FOUND)