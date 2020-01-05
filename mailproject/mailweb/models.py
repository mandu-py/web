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
    recipient = models.ForeignKey('Userinfo', on_delete=models.DO_NOTHING , to_field='mailaddress', db_column='recipient')
    datedb = models.DateTimeField()
    checkdb = models.IntegerField()

    select_openmail = (
        (1,'미열람'),
        (2,'열람후미신고'),
        (3,'열람후신고')
    )
    openmail = models.IntegerField(choices=select_openmail)

    

    class Meta:
        managed = False
        db_table = 'maildata'


class Userinfo(models.Model):
    idx = models.AutoField(primary_key=True)
    mailaddress = models.CharField(max_length=100,unique=True )
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'userinfo'


