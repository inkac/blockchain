from django.shortcuts import render
from django.http import HttpResponse
from transaction.models import Transaction
from blockchain.models  import Block
import datetime
import json
from hashlib import sha256

class Block_struct:  
    difficulty = 2    # difficulty of PoW algorithm
    def __init__(self, index, timestamp, transactions, previous_hash, nonce = 0):
        self.index = index 
        self.timestamp = timestamp
        self.transactions = transactions 
        self.previous_hash = previous_hash 
        self.nonce = nonce
    def compute_hash(self):  
        block_string = json.dumps(self.__dict__, sort_keys=True) 
        return sha256(block_string.encode()).hexdigest()
    def proof_of_work(self): 
        self.nonce = 0
        computed_hash = self.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty): 
            self.nonce += 1
            computed_hash = self.compute_hash()
        return computed_hash
def create_block(transactions_json):
    block_latest_db = Block.objects.latest('id')
    pre_timestamp = block_latest_db.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
    pre_block    = Block_struct(block_latest_db.id, pre_timestamp,
                  block_latest_db.transactions, block_latest_db.previous_hash, int(block_latest_db.nonce) )
    pre_block_hash = pre_block.compute_hash()
    this_timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
    this_block = Block_struct(pre_block.index + 1,  this_timestamp,
                  transactions_json,  pre_block_hash)
    this_hash = this_block.proof_of_work()
    Block.objects.create(id=this_block.index, timestamp=this_block.timestamp,
                  transactions = this_block.transactions, previous_hash = this_block.previous_hash,
                  nonce = this_block.nonce )
    return str(this_block.nonce) + "  :  " + pre_block_hash + "  ------  " + this_hash
def add_block():
    return 0
def start(request):
    transactions_todo = Transaction.objects.filter(status=0).order_by('id')[:100]
    if 0 == len(transactions_todo):
        return HttpResponse("No transactions to process! wait for a new transaction...")
    ts_list = []
    for ts in transactions_todo:
        ts.status = 1; ts.save();
        ts_timestamp = ts.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
        ts_dict = {'type':ts.type, 'contents':ts.contents, 'nonce':ts.nonce, 'hash':ts.hash, 
                   'pubkey':ts.pubkey, 'signature':ts.signature, 'timestamp':ts_timestamp}
        ts_list.append(ts_dict)
    transactions_json = json.dumps(ts_list)
    html = create_block(transactions_json);
    return HttpResponse(html)

# Create your views here.
