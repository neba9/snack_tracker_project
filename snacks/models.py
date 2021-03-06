from django.db import models
from django.contrib.auth import get_user_model

class snacks(models.Model):
  name = models.CharField(max_length=64)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=255)

  def __str__(self):
    return self.name

# Create your models here.
