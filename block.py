import json
from sys import getsizeof as sizeof
from datetime import datetime
from merkletree import merkle, isPow2
from transaction import Transaction
from miner import Miner

class Block:

    def __init__(self, transactions, difficulty, version,  hash=None, nonce=None, previous=None, root=None,
                 timestamp=datetime.now().strftime('%d/%m/%Y,%H:%M:%S'), quantity=0, size=0):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            miner = Miner()
            self.version = version
            self.timeStamp = timestamp
            self.nonce = nonce  # int 1
            self.hash = hash  # hash 1
            self.transactions = transactions
            self.quantity = quantity  # int 2
            self.previous = previous  # hash 2
            self.root = root  # hash 3
            self.difficulty = difficulty  # int 3
            self.size = size  # int 4

            if quantity == 0:
                self.quantity = len(transactions)

            if root is None:
                self.root = merkle(transactions)

            if size == 0:
                self.size = sizeof(self.timeStamp) + sizeof(self.version) + sizeof(int) * 4 + sizeof(transactions) \
                            + sizeof(root) * 3

            if nonce is None:
                nonce, digest = miner.mine(self.timeStamp, self.root, self.quantity, self.size, self.difficulty)
                self.nonce = nonce
                self.hash = digest



        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512, " +
                            "encontrado {}".format(len(transactions)))

    def toString(self):
        return 'timestamp: {} hash: {} nonce: {} root: {} transactions: {} size: {}'.format(
            self.timeStamp, self.hash, self.nonce, self.root, self.quantity, self.size)

    def toJson(self):
        return json.dumps({'version': self.version,
                           'timeStamp': self.timeStamp,
                           'nonce': self.nonce,
                           'quantity': self.quantity,
                           'hash': self.hash,
                           'previous': self.previous,
                           'root': self.root,
                           'difficulty': self.difficulty,
                           'size': self.size,
                           'transactions': [t.toJson() for t in self.transactions]
                           },
                          indent=4,
                          )


if __name__ == '__main__':
    trans = []
    for i in range(4):
        t1 = Transaction('1234543', 'dedasdeasd', 18.1, 'daedjkljkd', 'dadeokogj', 'lkjoeas')
        trans.append(t1)

    b1 = Block(trans, 12, 'sdaekdaklelas', 2)
    print(b1.toJson())