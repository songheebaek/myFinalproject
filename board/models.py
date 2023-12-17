from django.db import models

# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class userAccount(models.Model):
    uaerId = models.CharField(max_length=30)
    userPassword = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    birthday = models.CharField(max_length=8)
    gender = models.CharField(max_length=2)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=11)