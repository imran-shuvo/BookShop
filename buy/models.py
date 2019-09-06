from django.db import models
from django.contrib.auth.models import User
from book.models import BookInfo

class BuyRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    amount =models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class BuyTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    num_book = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True )
    def __str__(self):
        return str(self.user)
