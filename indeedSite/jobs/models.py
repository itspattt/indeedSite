from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return str(self.id) + ' - ' + self.name