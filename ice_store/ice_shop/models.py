from django.db import models

# Create your models here.


class Icecream(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100)
    ice_cream = models.ForeignKey(Icecream,on_delete=models.CASCADE,related_name='ice_cream')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']