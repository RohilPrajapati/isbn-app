from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    pages = models.IntegerField(null=True)
    isbn = models.CharField(max_length=60)
    short_description = models.TextField()
    publisher = models.CharField(max_length=150, null=True)
    source = models.URLField(null=True)
