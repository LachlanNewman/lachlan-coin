#Karl CHEN, 20/05/2017
#!/user/bin/python3

import shelve
import json

#initialise first block
def firstblock():
    #initial amount of coins in an account
    firstaccount = input('initial account: ')
    firstamount = input('initial coins in first block: ')
    
    #initial the hash of first block with 256 zeros
    zeros = [0]*256
    first_hash = ''.join(str(i) for i in zeros)
    
    #detail of first block initialisazion
    initial_coin = {}
    initial_coin['height'] = '1'
    initial_coin['sender'] = 'blockchan'
    initial_coin['receiver'] = firstaccount
    initial_coin['amount'] = firstamount
    initial_coin['signature'] = 'from other function' ###is there signature in 1s block? wait to change
    initial_coin['hash'] = first_hash
    initial_coin['previous_hash'] = 'null'

    #store first block in a blockchain dict
    blockchain = shelve.open('blockchain')
    blockchain['1'] = initial_coin
    blockchain.close()

class block:
    from_account = ''
    to_account = ''
    amount = 0
    signature = ''
    block_hash = ''
    nonce = ''

    def __init__(self, blockhash, blocknonce):
        #get transaction detail from .json
        transaction = open('trans.json')
        transdetail = json.load(transaction)
        transaction.close()
        
        self.from_account = transdetail['Sender']#from wallet
        self.to_account = transdetail['Recipient']#from wallet
        self.amount = transdetail['Amount']#from wallet
        self.signature = transdetail['Signature']#from wallet
        self.block_hash = blockhash###from crypto function
        self.nonce = blocknonce###should nonce generated by blockchain?

    def createblock(self):  
        #count the height of blockchain and get the number of new block
        blockchain = shelve.open('blockchain')
        height = len(blockchain) + 1

        #get the id of previous block
        prev_hash = blockchain[str(height - 1)]['hash']
        blockchain.close()

        #detail of a block
        block = {}
        block['height'] = height
        block['sender'] = self.from_account
        block['receiver'] = self.to_account
        block['amount'] = self.amount
        block['signature'] = self.signature
        block['hash'] = self.block_hash
        block['prev_hash'] = prev_hash

        return block

    def addblock(self):
        #add block to blockchain
        blockchain = shelve.open('blockchain')
        height = len(blockchain) + 1
        blockchain.update({str(height):self.createblock()})
        blockchain.close()
