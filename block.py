import json
from sys import getsizeof as size
from datetime import datetime
from merkletree import merkle, isPow2
from transaction import Transaction

class Block:

    def __init__(self, transactions, nonce, hash, difficulty, previous=None, root=merkle(transactions),
                 timestamp=datetime.now().strftime('%d%m%Y')):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            self.timeStamp = timestamp
            self.nonce = nonce
            self.transactions = transactions
            self.quantity = len(transactions)
            self.hash = hash
            self.previous = previous
            self.root = root
            self.difficulty = difficulty
            self.size = size(self.timeStamp) + size(self.nonce) + size(transactions) + size(self.quantidade) \
                             + size(self.hash) * 2 + size(self.raizMerkle) + size(dificuldade)

        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512")

    def toString(self):
        return 'timestamp: {} hash: {} nonce: {} root: {} transactions: {} size: {}'.format(
            self.timeStamp, self.hash, self.nonce, self.raizMerkle, self.quantidade, self.blockSize)

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