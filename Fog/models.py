from django.db import models


# Create your models here.
class UserInfo(models.Model):
    loginid = models.CharField(max_length=200, default="a")
    passwd = models.CharField(max_length=200, default="a")
    imsi = models.CharField(max_length=200, default="111111111111111")
    autn = models.CharField(max_length=200, default="11")
    rand = models.CharField(max_length=200, default="11")
    k = models.CharField(max_length=200, default="11")
    sqn = models.CharField(max_length=200, default="11")
    amf = models.CharField(max_length=200, default="11")
    op = models.CharField(max_length=200, default="11")
    opc = models.CharField(max_length=200, default="11")
    xres = models.CharField(max_length=200, default="11")
    kasme = models.CharField(max_length=200, default="11")
