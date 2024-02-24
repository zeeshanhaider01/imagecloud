from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class picture(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    picture=models.URLField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)