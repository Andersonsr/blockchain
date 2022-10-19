import json
from sys import getsizeof as sizeof
from datetime import datetime
from merkletree import merkle, isPow2
from transaction import Transaction
from miner import Miner

class Block:

    def __init__(self, transactions, difficulty, version,  hash=None, nonce=None, previousHash=None, merkleRoot=None,
                 timestamp=datetime.now().strftime('%d/%m/%Y,%H:%M:%S'), transactionsNumb=0, size=0):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            miner = Miner()
            self.version = version
            self.timeStamp = timestamp
            self.nonce = nonce  # int 1
            self.hash = hash  # hash 1
            self.transactions = transactions
            self.transactionsNumb = transactionsNumb  # int 2
            self.previousHash = previousHash  # hash 2
            self.merkleRoot = merkleRoot  # hash 3
            self.difficulty = difficulty  # int 3
            self.size = size  # int 4

            if transactionsNumb == 0:
                self.transactionsNumb = len(transactions)

            if merkleRoot is None:
                self.merkleRoot = merkle(transactions)

            if size == 0:
                self.size = sizeof(self.timeStamp) + sizeof(self.version) + sizeof(int) * 4 + sizeof(self.transactions) \
                            + sizeof(self.merkleRoot) * 3

            if nonce is None:
                nonce, digest = miner.mine(self.timeStamp, self.merkleRoot, self.transactionsNumb, self.size,
                                           self.difficulty)
                self.nonce = nonce
                self.hash = digest



        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512, " +
                            "encontrado {}".format(len(transactions)))

    def toString(self):
        return 'timestamp: {} hash: {} nonce: {} root: {} transactions: {} size: {}'.format(
            self.timeStamp, self.hash, self.nonce, self.merkleRoot, self.transactionsNumb, self.size)

    def toJson(self):
        return json.dumps({
                           'version': self.version,
                           'timeStamp': self.timeStamp,
                           'nonce': self.nonce,
                           'transactionsNumb': self.transactionsNumb,
                           'hash': self.hash,
                           'previousHash': self.previousHash,
                           'merkleRoot': self.merkleRoot,
                           'difficulty': self.difficulty,
                           'size': self.size,
                           'transactions': [t.toJson() for t in self.transactions]
                           }, indent=4)
