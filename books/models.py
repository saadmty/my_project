
from django.db import models
from django.urls import reverse

class Book(models.Model):
    model=models.CharField(max_length=30,null=True)
    Qty=models.IntegerField(default='20')
    Price=models.IntegerField(null=True,default='330')
    image=models.ImageField(upload_to="img/%y")


    def __str__(self):
        return self.model


