from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=500)
    createdOn = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=200)
    createdOn = models.DateTimeField(auto_now_add=True)


class IP(models.Model):
    ipAdress = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    modifiedOn = models.DateTimeField(null=True)