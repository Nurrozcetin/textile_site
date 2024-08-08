from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=10, default="")
    def __str__(self):
        return self.size

class Item(models.Model):
    title = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100, default="")
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='items', blank=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField()
    color = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    size = models.ManyToManyField(Size, related_name='items', blank=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title

