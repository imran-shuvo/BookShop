from django import forms
from .models import BuyRecord
from django.contrib import admin

class AddBuyRecord(forms.ModelForm):
    class Meta:
        model = BuyRecord
        fields = ['user','book']
