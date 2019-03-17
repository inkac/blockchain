from django.db import models

class Transaction(models.Model):
    type = models.CharField(max_length=200) #paper_submit, paper_comment, 
    timestamp = models.DateTimeField()
    contents  = models.TextField()
    nonce     = models.IntegerField(default = 0)
    hash      = models.CharField(max_length=200)
    signature = models.CharField(max_length=500)
    pubkey    = models.CharField(max_length=500)
    status    = models.IntegerField(default = 0) #0:new, 1:finished, 2:not valid, ...

