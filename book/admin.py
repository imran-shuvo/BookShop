from django.contrib import admin
from .models import BookCategory,BookInfo



class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('book_name','author','book_price','book_cat','book_available')

# Register your models here.
admin.site.register(BookCategory)
admin.site.register(BookInfo,BookInfoAdmin)
