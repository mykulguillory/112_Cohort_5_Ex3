from django.db import models

'''
field:
    Char
    Int
    Float
    Boolean

'''

#MIgration steps:
#1 - Make migrations
#2 - Apply Migrations

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 225)

    def __str__(self):
        return self.name 

class Movie(models.Model):
    title = models.CharField(max_length = 225)
    star = models.CharField(max_length = 225)
    release_year = models.IntegerField()
    price = models.FloatField()
    in_stock = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    in_4K = models.BooleanField()
    director = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.release_year) + self.title




