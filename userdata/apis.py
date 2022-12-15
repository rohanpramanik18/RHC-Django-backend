from rest_framework import views, response, exceptions, permissions
from rest_framework.decorators import api_view
from .serializer import UserSerializer as user_serializer, AshaSerializer, PatientSerializer as patient_serializer
from . import services, authentication


#FOR ADMIN USER
class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)
        print(data)
        return response.Response(data=serializer.data)
    
    
    
class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        token = services.create_token(user_id=user.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        return resp
    
    
class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = user_serializer.UserSerializer(user)
        return response.Response(serializer.data)
    
    
class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Adios"}
        return resp
    

    
#FOR ASHA WORKER
class AshaRegisterApi(views.APIView):
    def post(self, request):
        serializer = AshaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_ashauser(asha_dc=data)
        print(data)
        return response.Response(data=serializer.data)
    
    
    
class AshaLoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        ashauser = services.ashauser_email_selector(email=email)
        if ashauser is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not ashauser.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        token = services.create_ashatoken(user_id=ashauser.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        return resp
    
    
class AshaUserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        ashauser = request.user
        serializer = asha_serializer(ashauser)
        return response.Response(serializer.data)
    
    
class AshaLogoutApi(views.APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Adios"}
        return resp
    
    
    
    
# FOR PATIENT      
  
class PatientRegisterApi(views.APIView):
    def post(self, request):
        serializer = patient_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_patientuser(patient_dc=data)
        print(data)
        return response.Response(data=serializer.data)
    
    
    
class PatientLoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        patient = services.patient_email_selector(email=email)
        if patient is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not patient.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        token = services.create_ashatoken(patient_id=patient.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        return resp
    
    
class PatientUserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        patient = request.user
        serializer = asha_serializer.AshaSerializer(patient)
        return response.Response(serializer.data)
    
    
class PatientLogoutApi(views.APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Adios"}
        return resp