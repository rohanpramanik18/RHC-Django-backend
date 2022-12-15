from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
from rest_framework import status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import views, response, exceptions, permissions
from rest_framework.response import Response

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer, AshaSerializer
from .models import User, UserManager, Asha, Patient
from .serializer import UserSerializer as user_serializer, AshaSerializer as asha_serializer, PatientSerializer as patient_serializer
from . import services
from .services import UserDataClass, AshaDataClass, PatientDataClass


@api_view(['POST'])
def add_users(request):
    serializer = user_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    serializer.instance = services.create_user(user_dc=data)
        
    print(data)
        
    return response.Response(data=serializer.data)
   
    # validating for already existing data
    # if User.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
    
    # if user.is_valid():
    #     print("hello")
    #     user.save()
    #     print("hello")
    #     return JsonResponse(user.data, safe=False)
    # else:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def view_users(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        users = User.objects.filter(**request.query_param.dict())
    else:
        users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    # if there is something in items else raise error
    if users:
        return JsonResponse(serializer.data, safe=False)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_users(request, pk):
    user = User.objects.get(pk=pk)
    data = UserSerializer(instance=user, data=request.data)
  
    if data.is_valid():
        # data.save()
        print(request.data)
        services.modify_user(user_id=pk, user_dc = request.data)
        return Response(request.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# def put(self, request, status_id):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.instance = services.modify_user(
#         user=request.user, status_id=status_id, status_data=status
#         )
 
@api_view(['DELETE'])       
def delete_users(request, user_id):
    services.delete_user(user = request.user, user_id = user_id)
    
    return Response(status=status.HTTP_202_ACCEPTED)
    
    
    
#ASHA CRUD
    
    
@api_view(['POST'])
def add_ashausers(request):
    serializer = asha_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    serializer.instance = services.create_ashauser(asha_dc=data)
        
    print(data)
        
    return response.Response(data=serializer.data)

    
@api_view(['GET'])
def view_ashausers(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        ashausers = Asha.objects.filter(**request.query_param.dict())
    else:
        ashausers = Asha.objects.all()

    serializer = AshaSerializer(ashausers, many=True)
    # if there is something in items else raise error
    if ashausers:
        return JsonResponse(serializer.data, safe=False)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_ashausers(request, pk):
    ashauser = Asha.objects.get(pk=pk)
    data = AshaSerializer(instance=ashauser, data=request.data)
  
    if data.is_valid():
        # data.save()
        print(request.data)
        services.modify_ashauser(asha_id=pk, asha_dc = request.data)
        return Response(request.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# def put(self, request, status_id):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.instance = services.modify_user(
#         user=request.user, status_id=status_id, status_data=status
#         )
 
@api_view(['DELETE'])       
def delete_ashausers(request, asha_id):
    services.delete_ashauser(ashauser = request.user, asha_id = asha_id)
    
    return Response(status=status.HTTP_202_ACCEPTED)






@api_view(['POST'])
def add_patients(request):
    serializer = patient_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    services.create_patient(patient_dc=data)
        
    print(data)
        
    return response.Response(data=serializer.data)

# VIEW LINES 175-178 not working    
# @api_view(['GET'])
# def view_patients(request):
    
#     # checking for the parameters from the URL
#     if request.query_params:
#         patients = Patient.objects.filter(**request.query_param.dict())
#     else:
#         patients = Patient.objects.all()

#     serializer = patient_serializer(patients, many=True)
#     # if there is something in items else raise error
#     if patients:
#         return JsonResponse(serializer.data, safe=False)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_patients(request, pk):
    patient = Patient.objects.get(pk=pk)
    data = patient_serializer(instance=patient, data=request.data)
  
    if data.is_valid():
        # data.save()
        print(request.data)
        services.modify_patient(patient_id=pk, patient_dc = request.data)
        return Response(request.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# def put(self, request, status_id):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.instance = services.modify_user(
#         user=request.user, status_id=status_id, status_data=status
#         )
 
@api_view(['DELETE'])       
def delete_patients(request, patient_id):
    services.delete_patient(patient = request.user, patient_id = patient_id)
    
    return Response(status=status.HTTP_202_ACCEPTED)