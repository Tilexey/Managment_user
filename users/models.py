from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
