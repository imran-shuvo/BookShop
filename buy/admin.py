from django.contrib import admin
from .models import BuyRecord,BuyTotal

class AdminBuyRecord(admin.ModelAdmin):
    readonly_fields = ('date',)
class AdminBuyTotal(admin.ModelAdmin):
    readonly_fields = ('date',)




admin.site.register(BuyRecord,AdminBuyRecord)
admin.site.register(BuyTotal,AdminBuyTotal)
