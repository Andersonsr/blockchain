import json
from sys import getsizeof as sizeof
from datetime import datetime
from merkletree import merkle, isPow2
from transaction import Transaction

class Block:

    def __init__(self, transactions, nonce, hash, difficulty, previous=None, root=None,
                 timestamp=datetime.now().strftime('%d/%m/%Y,%H:%M:%S'), quantity=0, size=0):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            self.timeStamp = timestamp
            self.nonce = nonce
            self.transactions = transactions
            self.quantity = quantity
            if quantity == 0:
                self.quantity = len(transactions)
            self.hash = hash
            self.previous = previous
            if root is None:
                root = merkle(transactions)
            self.root = root
            self.difficulty = difficulty
            self.size = size
            if size == 0:
                self.size = sizeof(self.timeStamp) + sizeof(self.nonce) + sizeof(self.transactions) + sizeof(self.quantity) + sizeof(self.hash) * 2 + sizeof(self.root) + sizeof(self.difficulty)

        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512, " +
                            "encontrado {}".format(len(transactions)))

    def toString(self):
        return 'timestamp: {} hash: {} nonce: {} root: {} transactions: {} size: {}'.format(
            self.timeStamp, self.hash, self.nonce, self.root, self.quantity, self.size)

    def toJson(self):
        return json.dumps({'timeStamp': self.timeStamp,
                           'nonce': self.nonce,
                           'transactions': [t.toJson() for t in self.transactions],
                           'quantity': self.quantity,
                           'hash': self.hash,
                           'previous': self.previous,
                           'root': self.root,
                           'difficulty': self.difficulty,
                           'size': self.size
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