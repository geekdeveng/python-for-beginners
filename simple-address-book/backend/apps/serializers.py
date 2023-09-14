from rest_framework import serializers
from .models import Contact, Label, ContactLabel, AdditionalInfo

class ContactLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLabel
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    contact_label = ContactLabelSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = '__all__'

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    contact_label = ContactLabelSerializer(many=True, read_only=True)
    additional_info = AdditionalInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
