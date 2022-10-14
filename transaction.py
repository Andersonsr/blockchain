import json


class Transaction:

    def __init__(self, origem, destino, valor, troco, signOrigem, signDestino):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.troco = troco
        self.signOrigem = signOrigem
        self.signDestino = signDestino

    def toString(self):
        return '{}{}{}{}{}{}'.format(self.origem, self.destino, str(self.valor), self.troco, self.signOrigem,
                                     self.signDestino)

    def toJson(self):
        return json.dumps({'origem': self.origem,
                           'destino': self.destino,
                           'valor': self.valor,
                           'troco': self.troco,
                           'signOrigem': self.signOrigem,
                           'signDestino': self.signDestino},
                          indent=4
                          )


if __name__ == '__main__':
    t1 = Transaction('1234543', 'dedasdeasd', 18.1, 'daedjkljkd', 'dadeokogj', 'lkjoeas')
    print(t1.toJson())