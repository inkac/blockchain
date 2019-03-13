from django.shortcuts import render
from django.http import HttpResponse
from .models import Block
import datetime
from hashlib import sha256
from django.db.models import Max

def index(request):
    latest_block_list = Block.objects.order_by('-id')[:10]
    output = ''
    for q in latest_block_list:
        output += str(q.id) + ': \n ' + q.transactions + ',\n\n'
    return HttpResponse(output)

def read(request, block_id):
    return HttpResponse("Get block info:  %s." % block_id)

def write(request):
    latest_block= Block.objects.latest('id')
    hash_string = latest_block.transactions + str(latest_block.timestamp)
    hash_value  = sha256(hash_string.encode(encoding='UTF-8')).hexdigest()
    new_block   = Block.objects.create(timestamp = str(datetime.datetime.utcnow()), transactions = 'asdfasdfasdf', previous_hash = hash_value )
    return HttpResponse("Write a block:   %s." % new_block.id)
