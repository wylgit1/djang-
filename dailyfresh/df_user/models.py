from django.db import models

# Create your models here.
class UserInfo(models.Models):
	uname = models.CharField(max_length=25)
	upwd = models.CharField(max_length=40)
