from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Snack(models.Model):
    name= models.CharField(max_length=255, null=False, blank=True)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField()
