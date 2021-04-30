from django.db import models


# Create your models here.

class MyUser(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
