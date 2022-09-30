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

    def mine(self, transactions):
        i = 0
        while True:
            input = ''
            for t in transactions:
                input += t.stringfi()

            input += str(i)
            digest = sha256(input.encode()).hexdigest()
            if self.check(digest):
                return i, digest

            i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dificuldade', default=4, type=int)
    parser.add_argument('-b', dest='blocos', default=10, type=int)
    args = parser.parse_args()

    blockchain = chain()
    miner1 = miner(args.dificuldade)
    for i in range(args.blocos):
        print('gerando bloco ' + str(i+1) + '...')
        transactions = []
        pow2 = [2**i for i in range(1, 10)]
        n = pow2[randint(0, len(pow2)-1)]
        for j in range(n):
            origem = sha256(str(randint(0, 100)).encode()).hexdigest()
            destino = sha256(str(randint(100, 200)).encode()).hexdigest()
            troco = sha256(str(randint(0, 200)).encode()).hexdigest()
            valor = randint(100, 1000)
            transactions.append(transaction(origem, destino, valor, troco))

        nonce, digest = miner1.mine(transactions)
        b = block(transactions, nonce, digest)
        blockchain.addBlock(b)
        print('bloco {} gerado com sucesso! hash: {}\n'.format(i+1, digest))

    print('cadeia de blocos:')
    blockchain.printAll()
