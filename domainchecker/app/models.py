from django.db import models
from django.contrib.auth.models import User

class Path(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    path = models.CharField(max_length=2000)
