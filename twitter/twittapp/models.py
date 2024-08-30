from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Twitt(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.TextField(max_length=500 , null=True ,blank=True)
    photo = models.ImageField(upload_to='photos/', null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
