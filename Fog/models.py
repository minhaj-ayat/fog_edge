from django.db import models


# Create your models here.
class UserInfo(models.Model):
    loginid = models.CharField(max_length=200, default="a")
    passwd = models.CharField(max_length=200, default="a")
    imsi = models.CharField(max_length=200, default="a")
    autn = models.CharField(max_length=200, default="a")
    rand = models.CharField(max_length=200, default="a")
    xres = models.CharField(max_length=200, default="a")
    kasme = models.CharField(max_length=200, default="a")
