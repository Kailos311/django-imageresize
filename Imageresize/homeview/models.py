from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    path = models.ImageField(upload_to='uploads/')

def __str__(self):
     return self.title