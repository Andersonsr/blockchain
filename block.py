from datetime import datetime
from merkletree import merkle, isPow2

class transaction:
    counter = 1

    def __init__(self, origem, destino, valor, troco):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.troco = troco
        self.id = transaction.counter
        transaction.counter += 1

    def stringfi(self):
        return self.origem + self.destino + str(self.valor) + str(self.id)

class block:
    def __init__(self, transactions, nonce, hash):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            self.timeStamp = datetime.now()
            self.nonce = nonce
            self.transactions = transactions
            self.quantidade = len(transactions)
            self.hash = hash
            self.anterior = None
            self.raizMerkle = merkle(transactions)

        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512")

    def stringfi(self):
        return 'hash: ' + self.hash + ' timestamp: ' + str(self.timeStamp) + ' nonce: ' + \
               str(self.nonce) + ' quantidade de transacoes: ' + str(self.quantidade) + ' raiz merkle: ' \
               + self.raizMerkle

