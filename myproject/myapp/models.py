from django.db import models

class Tree(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
