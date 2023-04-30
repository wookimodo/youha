from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 유튜버
class Youtuber(models.Model):
    name = models.CharField(max_length=200,default='')
    subscribers = models.IntegerField(default=0, null=True)
    link = models.TextField(default=None)
    imgUrl = models.TextField(default=None)

    class Meta:
        db_table='Youtuber'

# 댓글
class Comment(models.Model):
    name = models.ForeignKey('Youtuber',on_delete=models.CASCADE)
    videoId = models.CharField(max_length=100,default='')
    author = models.CharField(max_length=100,default='')
    comment = models.TextField(default=None)
    sentiment = models.CharField(max_length=30,default='')
    score = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(1.0)])
    date = models.CharField(max_length=100,default='')
