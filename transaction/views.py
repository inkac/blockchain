from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction
from hashlib import sha256
import datetime

def index(request):
    latest_transaction_list = Transaction.objects.order_by('-id')[:10]
    output = ''
    for q in latest_transaction_list:
        output += str(q.id) + ': \n ' + q.contents + ',\n\n'
    return HttpResponse(output)

def new(request):
    ts_type = "paper_commit"
    ts_contents = "paper_commit_contents"
    hash_string = "hash tring"
    hash_value  = sha256(hash_string.encode(encoding='UTF-8')).hexdigest()
    new_transaction = Transaction.objects.create(type = ts_type ,timestamp = str(datetime.datetime.utcnow()), contents = ts_contents , hash = hash_value )
    return HttpResponse("submit a transaction and wait for blockchain acception: %s." % new_transaction.id)

# Create your views here.
