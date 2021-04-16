from django.db import models


# Create your models here.
class Mapper(models.Model):
    imsi = models.CharField(max_length=200, default="111")
    loginid = models.CharField(max_length=200, default="a")
    passwd = models.CharField(max_length=200, default="a")
