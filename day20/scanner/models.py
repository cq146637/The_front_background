from django.db import models

# Create your models here.


class type(models.Model):
    category = models.CharField(max_length=64,null=False)

class website(models.Model):
    url = models.CharField(unique=True,max_length=255,null=False)
    ip = models.CharField(default="0.0.0.0",max_length=32)
    port = models.IntegerField(default=80)
    name = models.CharField(max_length=255,null=False)
    types = models.ForeignKey(to="type",to_field="id",default=1)
    verbose = models.CharField(max_length=1024)
    # ctime = models.TimeField(auto_now=True)

class scan_times(models.Model):
    time = models.CharField(db_index=True,max_length=255,null=True)
    websites = models.ForeignKey(to="website",to_field="id")
    status = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
