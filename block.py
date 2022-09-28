from time import time
from hashlib import sha256
class transaction:
    counter = 1

    def __init__(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.id = transaction.counter
        transaction.counter += 1

    def stringfi(self):
        return self.origem + self.destino + str(self.valor)

class block:
    def __init__(self, transaction, nonce, hash):
        self.timeStamp = time()
        self.nonce = nonce
        self.transaction = transaction
        self.hash = hash
        self.anterior = None

    def stringfi(self):
        return 'hash: ' + self.hash + ' timestamp: ' + str(self.timeStamp) + ' nonce: ' + \
               str(self.nonce) + ' origem: ' + self.transaction.origem + ' destino: ' + \
               self.transaction.destino + ' valor: ' + str(self.transaction.valor)
