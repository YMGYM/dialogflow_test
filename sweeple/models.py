from django.db import models

# Create your models here.

class Sweeple(models.Model):
    taste = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.taste
    
    
class Delivery(models.Model):
    taste = models.CharField(max_length=20)
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name