from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    #yeni özellikler eklenebilir

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    date = models.DateField(auto_now=True)
    user = models.CharField(max_length=255)
    customer = models.ManyToManyField(Customer, blank=True)
    orderNo = models.CharField(max_length=255, null=True, blank=True)  
    model = models.TextField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    supplier = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    errorSource = models.TextField(null=True, blank=True)
    detectionMethod = models.TextField(null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    actionForRepeat = models.TextField(null=True, blank=True)


class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")