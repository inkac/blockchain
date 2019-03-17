# Create your models here.
from django.db import models

class Block(models.Model):
    previous_hash = models.CharField(max_length=200)
    timestamp     = models.DateTimeField()
    transactions  = models.TextField()
    nonce         = models.IntegerField(default = 0)

