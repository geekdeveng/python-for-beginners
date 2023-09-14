from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Contact, Label, AdditionalInfo, ContactLabel
from .serializers import ContactSerializer, LabelSerializer, AdditionalInfoSerializer, ContactLabelSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'email', 'phone_number']
    pagination_class = PageNumberPagination

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class AdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer

class ContactLabelViewSet(viewsets.ModelViewSet):
    queryset = ContactLabel.objects.all()
    serializer_class = ContactLabelSerializer