from django.db import models

class UserDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class option(models.Model):
    id = models.BigAutoField(primary_key=True)
    option = models.CharField(max_length=100)

class Details:
    email : str
    password : str

class Compose:
    recipient : str
    subject : str
    body : str