from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
