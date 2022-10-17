import os
import json
from block import Block
from transaction import Transaction

class Chain:
    def __init__(self):
        self.lastBlock = ''
        self.blocks = {}

    def addBlock(self, block):
        block.previous = self.lastBlock
        self.lastBlock = block.hash
        self.blocks[block.hash] = block

    def getBlock(self, hash):
        return self.blocks[hash]

    def getLastBllock(self):
        return self.blocks[self.lastBlock]

    def saveAsJson(self, folder):
        next = self.lastBlock
        if not os.path.exists('blocks/{}/'.format(folder)):
            os.makedirs('blocks/{}/'.format(folder))
        file = open('blocks/{}/lastBlock.txt'.format(folder), 'w+')
        file.write(self.lastBlock)
        file.close()
        while next != '':
            block = self.blocks[next]
            file = open('blocks/{}/{}.json'.format(folder, block.hash), 'w+')
            file.write(block.toJson())
            file.close()
            next = block.previous

    def loadChain(self, folder):
        if not self.blocks:
            file = open('blocks/{}/lastBlock.txt'.format(folder))
            self.lastBlock = file.readline()
            file.close()
            files = os.listdir('blocks/{}/'.format(folder))
            for filename in files:
                if '.json' in filename:
                    with open('blocks/{}/{}'.format(folder, filename)) as file:
                        transactions = []
                        data = json.load(file)
                        for t in data['transactions']:
                            newT = Transaction(t['sender'], t['recipient'], t['value'], t['change'], t['signSender'],
                                    t['signRecipient'])
                            transactions.append(newT)
                        block = Block(transactions=transactions, nonce=data['nonce'], hash=data['hash'],
                                      difficulty=data['difficulty'], timestamp=data['timeStamp'],
                                      previous=data['previous'], root=data['root'])
                        self.blocks[block.hash] = block

    def printAll(self):
        next = self.lastBlock
        while next != '':
            block = self.blocks[next]
            print('bloco:')
            print(block.toString())
            next = block.previous

