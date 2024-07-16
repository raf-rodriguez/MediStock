from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *

# User creation -----------------------------------------
class UserCreate(APIView): 
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAuthorization(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginAuthorization, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "user_id": token.user_id})
    
# Logout user
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response("Logged out successfully")
    
class AppUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AppUserSerializer

# Storage ------------------------------------------
class StorageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class UserStorageListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        storage = Storage.objects.filter(user_id=user_id)
        serializer = StorageSerializer(storage, many=True)
        return Response(serializer.data)

class LatestUserStorageListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        storage = Storage.objects.filter(user_id=user_id).order_by('-storage_id')[:5]
        serializer = StorageSerializer(storage, many=True)
        return Response(serializer.data)
    
# Medication ------------------------------------------
class MedicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

User = get_user_model()

class UserMedicationView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        medication = Medication.objects.filter(user_id=user_id)
        serializer = MedicationSerializer(medication, many=True)
        return Response(serializer.data)
    
class LatestUserMedicationListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        medication = Medication.objects.filter(user_id=user_id).order_by('-medication_id')[:5]
        serializer = MedicationSerializer(medication, many=True)
        return Response(serializer.data)
    
# Employee -----------------------------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserEmployeeView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        employee = Employee.objects.filter(user_id=user_id)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
class LatestUserEmployeeListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        employee = Employee.objects.filter(user_id=user_id).order_by('-employee_id')[:5]
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
