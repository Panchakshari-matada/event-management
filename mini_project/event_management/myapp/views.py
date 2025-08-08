from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Register, AddEvent
from .serializers import RegisterSerializer, AddEventSerializer

# ViewSet for Register Model
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

# ViewSet for AddEvent Model
class AddEventViewSet(viewsets.ModelViewSet):
    queryset = AddEvent.objects.all()
    serializer_class = AddEventSerializer