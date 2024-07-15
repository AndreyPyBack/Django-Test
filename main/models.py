from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    text_problem = models.TextField()
    data_problem = models.DateField()
    contact_info = models.CharField(max_length=255)