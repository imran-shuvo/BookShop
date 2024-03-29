from django.db import models

# Create your models here.
class BookCategory(models.Model):
    cat_name = models.CharField(max_length=30)


    def __str__(self):
        return self.cat_name



class BookInfo(models.Model):
    book_name = models.CharField(max_length=30)
    author  = models.CharField(max_length=30,null = True, blank = True)
    book_cat = models.ForeignKey(BookCategory,on_delete = None)
    book_price = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    book_available = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return self.book_name
