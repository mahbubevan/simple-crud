from django.db import models
# Create your models here.

class BookList(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
