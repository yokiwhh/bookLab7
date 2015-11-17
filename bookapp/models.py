from django.db import models
from django.contrib import admin
# Create your models here.
# -*- coding: utf-8 -*-
def decode(info):
      return info.decode('utf-8')
class Book(models.Model):
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = verbose_name
    ISBN = models.CharField('ISBN',max_length=500)
    title = models.CharField('title',max_length=200)
    author = models.CharField('author',max_length=60)
    price = models.CharField('price',max_length=60,blank=True)
    publisher = models.CharField('publisher',max_length=200,blank=True)
    pubdate = models.CharField('PublishDate',max_length=60,blank=True)

    def __unicode__(self):
        return str(self.title)

class Author(models.Model):
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = verbose_name
    Name = models.CharField('Name',max_length=60)
    Age = models.IntegerField('Age')
    Country = models.CharField('Country',max_length=60)

    def __unicode__(self):
        return str(self.Name)
