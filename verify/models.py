from django.db import models

# Create your models here.

class User_verify(models.Model):
    code = models.CharField(max_length=20, default=0)
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.code