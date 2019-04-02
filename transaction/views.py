from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import base64
import datetime
import json
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from hashlib import sha256


#@csrf_protect
def index(request):
    latest_transaction_list = Transaction.objects.order_by('-id')[:10]
    output = ''
    for q in latest_transaction_list:
        output += str(q.id) + ': \n ' + q.contents + ',\n\n'
    return HttpResponse(output)

@csrf_exempt
def revoke(request):
    id = 0;
    return HttpResponse("revoke a transaction and wait for blockchain acception: %s." % id)

@csrf_exempt
def new(request):
    if "POST" != request.method:
        return HttpResponse("not POST!")
    try:
        postBody = request.body
        #print(type(postBody),end='  :  '); print(postBody)
        post_contents = json.loads(postBody)   
        #print(type(post_contents),end=' : '); print(post_contents)
        #print(post_contents['type'])
        ts_type     = post_contents["type"]
        ts_contents = post_contents["contents"]
        ts_pubkey   = post_contents["pubkey"]
        ts_nonce    = post_contents["nonce"]
        ts_hash     = post_contents["hash"]
        ts_signature= post_contents["signature"]
    except:
        return HttpResponse("someting wrong with json.loads(postBody)!")

    hash_data = {'type':ts_type, 'contents':ts_contents, 'nonce':ts_nonce}
    hash_json = json.dumps(hash_data, sort_keys=True)
    pubKey = RSA.importKey(ts_pubkey)
    hash_obj = SHA256.new(hash_json.encode());
    verifier = PKCS1_v1_5.new(pubKey)
    if not verifier.verify(hash_obj, base64.b64decode(ts_signature)):
        #print("Check Signature failed!")
        return HttpResponse("Check Signature failed!")

    try:
        now_timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        new_transaction = Transaction.objects.create(type = ts_type ,timestamp = now_timestamp,
                               contents = ts_contents , hash = ts_hash, pubkey = ts_pubkey,
                               nonce = ts_nonce, signature = ts_signature )
    except:
        return HttpResponse("someting wrong with transaction writing!")
    return HttpResponse(0)
