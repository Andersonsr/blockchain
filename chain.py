import os
import json

class Chain:
    def __init__(self):
        self.lastBlock = ''
        self.blocks = {}

    def addBlock(self, block):
        block.anterior = self.lastBlock
        self.lastBlock = block.hash
        self.blocks[block.hash] = block

    def getBlock(self, hash):
        return self.blocks[hash]

    def getLastBllock(self):
        return self.blocks[self.lastBlock]

    def saveAsJson(self, folder):
        next = self.lastBlock
        file = open('blocks/{}/lastBlock.txt'.format(folder), 'w+')
        file.write(self.lastBlock)
        file.close()
        while next != '':
            block = self.blocks[next]
            file = open('blocks/{}/{}.json'.format(folder, block.hash), 'w+')
            file.write(block.toJson())
            file.close()
            next = block.anterior

    def loadChain(self, folder):
        if not self.blocks:
            file = open('blocks/{}/lastBlock.txt'.format(folder))
            self.lastBlock = file.readline()
            file.close()
            files = os.listdir('blocks/{}/'.format(folder))
            for filename in files:
                data = json.load('blocks/{}/{}'.format(folder, filename))
                print(data)


    def printAll(self):
        next = self.lastBlock
        while next != '':
            block = self.blocks[next]
            print('bloco:')
            print(block.toString())
            next = block.anterior

