from django import forms
from .models import BuyRecord

class AddBuyRecord(object):
    class Meta:
        model = BuyRecord
        fields = ['user','book','amount','total']
