# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Log(models.Model):
    idx = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=50)

    class Meta:
        app_label = 'maildata'
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
        app_label = 'maildata'
        managed = False
        db_table = 'maildata'


class Userinfo(models.Model):
    idx = models.AutoField(primary_key=True)
    mailaddress = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'maildata'
        managed = False
        db_table = 'userinfo'
