from django.db import models

# Create your models here.

class Author(models.Model):
    # 出版社 [多]
    name = models.CharField('姓名',max_length=50)

class Book(models.Model):
    # 出版社 [多]
    title = models.CharField('书名',max_length=11)
    publisher = models.ManyToManyField(Author)