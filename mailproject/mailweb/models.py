from django.db import models

# Create your models here.
class Log(models.Model):
    idx = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'log'


class Maildata(models.Model):
    idx = models.AutoField(primary_key=True)
    indate = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    datedb = models.DateTimeField()
    checkdb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maildata'


class Userinfo(models.Model):
    idx = models.AutoField(primary_key=True)
    mailaddress = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'userinfo'
