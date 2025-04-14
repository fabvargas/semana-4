from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email