import os
import json
from block import Block
from transaction import Transaction

class Chain:
    def __init__(self, name='no name'):
        self.lastBlock = '0'
        self.blocks = {}
        self.name = name

    def addBlock(self, block):
        block.previousHash = self.lastBlock
        self.lastBlock = block.hash
        self.blocks[block.hash] = block

    def getBlock(self, hash):
        return self.blocks[hash]

    def getLastBllock(self):
        return self.blocks[self.lastBlock]

    def searchLastBlock(self):
        next = "0"
        oldNext = ''
        while next != oldNext:
            oldNext = next
            for key in self.blocks:
                if self.blocks[key].previousHash == next:
                    next = self.blocks[key].hash

        self.lastBlock = next

    def saveAsJson(self, folder):
        next = self.lastBlock
        if not os.path.exists('blocks/{}/'.format(folder)):
            os.makedirs('blocks/{}/'.format(folder))
        while next != '0':
            block = self.blocks[next]
            file = open('blocks/{}/{}.json'.format(folder, block.hash), 'w+')
            file.write(block.toJson())
            file.close()
            next = block.previousHash

    def loadChain(self, folder):
        if not self.blocks:
            files = os.listdir('blocks/{}/'.format(folder))
            for filename in files:
                if '.json' in filename:
                    with open('blocks/{}/{}'.format(folder, filename)) as file:
                        transactions = []
                        data = json.load(file)
                        for t in data['transactions']:
                            newT = Transaction(t['sender'], t['receiver'], t['value'], t['change'], t['senderSignature'],
                                    t['receiverSignature'])
                            transactions.append(newT)
                        block = Block(transactions, data['difficulty'], data['version'], nonce=data['nonce'],
                                      hash=data['hash'], timestamp=data['timeStamp'],
                                      previousHash=data['previousHash'], merkleRoot=data['merkleRoot'],
                                      transactionsNumb=data['transactionsNumb'], size=data['size'])
                        self.blocks[block.hash] = block
            self.searchLastBlock()

    def toHTML(self):
        next = self.lastBlock
        content = '<ul>'
        while next != '0':
            block = self.blocks[next]
            content += '<a href=\'/blockchains/{}/{}/\'><li>' \
                       '<p>hash:{}</p>' \
                       '<p>size:{}B</p>' \
                       '<p>difficulty:{}</p>' \
                       '<p>transactionNumber:{}</p>' \
                       '<p>merkleRoot:{}</p>' \
                       '<p>nonce:{}</p>' \
                       '</li></a>'.format(self.name, block.hash,  block.hash,
                                          block.size,
                                          block.difficulty,
                                          block.transactionsNumb,
                                          block.merkleRoot,
                                          block.nonce)
            next = block.previousHash

        return content + '</ul>'

    def printAll(self):
        next = self.lastBlock
        while next != '0':
            block = self.blocks[next]
            print('bloco:')
            print(block.toString())
            next = block.previousHash

