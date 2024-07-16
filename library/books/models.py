from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_data = models.DateField()
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return F"{self.title} - {self.author} - {self.isbn}"


