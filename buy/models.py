from django.db import models
from django.contrib.auth.models import User
from book.models import BookInfo

class BuyRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    total = models.IntegerField()


    def __str__(self):
        return self.user
