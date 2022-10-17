import json


class Transaction:

    def __init__(self, sender, recipient, value, change, signSender, signRecipient):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.change = change
        self.signSender = signSender
        self.signRecipient = signRecipient

    def toString(self):
        return '{}{}{}{}{}{}'.format(self.origem, self.destino, str(self.valor), self.troco, self.signOrigem,
                                     self.signDestino)

    def toJson(self):
        return {'sender': self.sender,
                'recipient': self.recipient,
                'value': self.value,
                'change': self.change.decode(),
                'signSender': self.signSender,
                'signRecipient': self.signRecipient}


if __name__ == '__main__':
    t1 = Transaction('1234543', 'dedasdeasd', 18.1, 'daedjkljkd', 'dadeokogj', 'lkjoeas')
    print(t1.toJson())
