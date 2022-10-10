from sys import getsizeof as size
from datetime import datetime
from merkletree import merkle, isPow2

class transaction:

    def __init__(self, origem, destino, valor, troco, signOrigem, signDestino):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.troco = troco
        self.signOrigem = signOrigem
        self.signDestino = signDestino

    def stringfi(self):
        return (str(self.origem.n) + str(self.destino.n) + str(self.valor) + self.troco).encode() \
               + self.signOrigem + self.signDestino

    def printable(self):
        return 'origem: ' + str(self.origem.n) + ' destino: ' + str(self.destino.n) + ' valor: ' + str(self.valor) \
               + ' troco: ' + self.troco


class block:
    def __init__(self, transactions, nonce, hash, dificuldade):
        if isPow2(len(transactions)) and len(transactions) <= 512:
            self.timeStamp = datetime.now()
            self.nonce = nonce
            self.transactions = transactions
            self.quantidade = len(transactions)
            self.hash = hash
            self.anterior = None
            self.raizMerkle = merkle(transactions)
            self.dificuldade = dificuldade
            self.blockSize = size(self.timeStamp) + size(self.nonce) + size(transactions) + size(self.quantidade)\
                             + size(self.hash)*2 + size(self.raizMerkle) + size(dificuldade)

        else:
            raise Exception("o numero de transacoes precisa ser potencia de 2, entre 2 e 512")

    def stringfi(self):
        return 'hash: ' + self.hash + ' timestamp: ' + str(self.timeStamp) + ' nonce: ' + \
               str(self.nonce) + ' quantidade de transacoes: ' + str(self.quantidade) + ' raiz merkle: ' \
               + self.raizMerkle + ' dificuldade: ' + str(self.dificuldade) + ' tamanho do bloco: ' \
               + str(self.blockSize)

