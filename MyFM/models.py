from django.db import models

# Create your models here.
class Recording(models.Model):
    # 4 genres and intervals
    genre1 = models.CharField(max_length=80)
    interval1 = models.IntegerField()
    genre2 = models.CharField(max_length=80)
    interval2 = models.IntegerField()
    genre3 = models.CharField(max_length=80)
    interval3 = models.IntegerField()
    genre4 = models.CharField(max_length=80)
    interval4 = models.IntegerField()

    #news and interval
    news = models.BooleanField()
    newsinterval = models.IntegerField()

    #jokes and riddles
    jokesinterval = models.IntegerField()
    riddlesinterval = models.IntegerField()