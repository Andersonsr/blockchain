import json
from sys import getsizeof as size
from datetime import datetime
from merkletree import merkle, isPow2
from transaction import Transaction

class Block:

    def __init__(self, transactions, nonce, hash, dificuldade):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            self.timeStamp = datetime.now().strftime('%d%m%Y')
            self.nonce = nonce
            self.transactions = transactions
            self.quantidade = len(transactions)
            self.hash = hash
            self.anterior = None
            self.raizMerkle = merkle(transactions)
            self.dificuldade = dificuldade
            self.blockSize = size(self.timeStamp) + size(self.nonce) + size(transactions) + size(self.quantidade) \
                             + size(self.hash) * 2 + size(self.raizMerkle) + size(dificuldade)

        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512")

    def toString(self):
        return 'timestamp: {} hash: {} nonce: {} root: {} blocks: {} size: {}'.format(
            self.timeStamp, self.hash, self.nonce, self.raizMerkle, self.quantidade, self.blockSize)

    def toJson(self):
        return json.dumps({'timestamp': self.timeStamp,
                           'nonce': self.nonce,
                           'transactions': [t.toJson() for t in self.transactions],
                           'quantidade': self.quantidade,
                           'hash': self.hash,
                           'anterior': self.anterior,
                           'raiz': self.raizMerkle,
                           'dificuldade': self.dificuldade,
                           'size': self.blockSize
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