from django.db import models

# Create your models here.

# Youtuber
class Youtuber(models.Model):
    name = models.CharField(max_length=200,default='')
    subscribers = models.IntegerField(default=0, null=True)
    link = models.TextField(default=None)
    imgUrl = models.TextField(default=None)

    class Meta:
        db_table='Youtuber'