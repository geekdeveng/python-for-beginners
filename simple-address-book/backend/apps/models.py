from django.db import models

# Create your models here.
class Contact(models.Model):
    profile_picture_url = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact'

class Label(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'label'

class ContactLabel(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    class Meta:
        db_table = 'contact_label'

class AdditionalInfo(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'additional_info'
