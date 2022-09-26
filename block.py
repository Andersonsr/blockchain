from time import time

class transaction:
    def __init__(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor

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
