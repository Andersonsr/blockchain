import argparse
from hashlib import sha256
from block import transaction, block
from chain import chain
from random import randint


class miner:
    def __init__(self, difculdade):
        self.dificuldade = difculdade

    def check(self, hash):
        for i in range(self.dificuldade):
            if hash[i] != str(0):
                return False
        return True

    def mine(self, transaction):
        i = 0
        while True:
            input = transaction.stringfi() + str(i)
            digest = sha256(input.encode()).hexdigest()
            if self.check(digest):
                return i, digest
            i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dificuldade', default=2, type=int)
    parser.add_argument('-b', dest='blocos', default=10, type=int)
    args = parser.parse_args()

    blockchain = chain()
    miner1 = miner(args.dificuldade)
    for i in range(args.blocos):
        origem = sha256(str(randint(0, 100)).encode()).hexdigest()
        destino = sha256(str(randint(100, 200)).encode()).hexdigest()
        valor = randint(100, 1000)
        tran = transaction(origem, destino, valor)
        nonce, digest = miner1.mine(tran)
        b = block(tran, nonce, digest)
        blockchain.addBlock(b)

    blockchain.printAll()
