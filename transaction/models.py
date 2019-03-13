from django.db import models

class Transaction(models.Model):
    type = models.CharField(max_length=200) #paper_submit, paper_comment, 
    timestamp = models.DateTimeField()
    contents  = models.TextField()
    hash      = models.CharField(max_length=200)

