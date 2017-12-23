from django.db import models

# Create your models here.



class User_type(models.Model):
    caption = models.CharField(max_length=32)
    

class User_info(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='User_type',to_field='id')
    
    