from .models import BookCategory,BookInfo
from django import forms


class AddCategory(forms.ModelForm):
    class Meta :
        model = BookCategory
        fields = ['cat_name']

class AddBook(forms.ModelForm):
    class Meta :
        model = BookInfo
        fields = ['book_name','author','book_price','book_cat','image']
