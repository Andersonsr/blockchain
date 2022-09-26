class chain:
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

    def printAll(self):
        next = self.lastBlock
        while next != '':
            block = self.blocks[next]
            print(block.stringfi())
            next = block.anterior