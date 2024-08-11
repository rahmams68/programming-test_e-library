from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, help_text='Enter a book title')
    author = models.CharField(max_length=64)
    summary = models.TextField(max_length=500)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='uploaded_images/')
    isbn = models.CharField(max_length=64)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return (f'"{self.title}" by {self.author}')

class Collection(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()