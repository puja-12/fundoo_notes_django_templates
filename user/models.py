from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=300)
    # first_name = models.CharField(max_length=100, null=True)
    # last_name = models.CharField(max_length=100, null=True)
    # email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)

    #
    # class Meta:
    #     db_table = 'user'


class MiddlewareDetails(models.Model):
    request_method = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    count= models.IntegerField(max_length=100)


