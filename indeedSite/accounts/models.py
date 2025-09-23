from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True, help_text="Comma-separated list of skills")
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"
