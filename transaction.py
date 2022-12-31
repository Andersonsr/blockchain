import json


class Transaction:

    def __init__(self, sender, receiver, value, change, senderSignature, receiverSignature):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.change = change
        self.senderSignature = senderSignature
        self.receiverSignature = receiverSignature

    def toString(self):
        return '{}{}{}{}{}{}'.format(self.sender, self.receiver, str(self.value), self.change, self.senderSignature,
                                     self.receiverSignature)

    def toJson(self):
        return {
                'sender': self.sender,
                'receiver': self.receiver,
                'value': self.value,
                'change': self.change,
                'senderSignature': self.senderSignature,
                'receiverSignature': self.receiverSignature
                }
