from math import log2
from block import Block
from userManager import Manager
from transaction import Transaction
from chain import Chain
from random import randint
import argparse
from merkletree import isPow2
from blockapp import blockApp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='minDifficulty', default=2, type=int, help='minimum difficulty')
    parser.add_argument('-m', dest='maxDifficulty', default=5, type=int, help='maximum difficulty')
    parser.add_argument('-b', dest='blocks', default=10, type=int, help='number of blocks')
    parser.add_argument('-o', dest='output', default='', type=str, help='output blockchain name')
    parser.add_argument('-i', dest='input', default='', type=str, help='blockchain to load')
    parser.add_argument('-t', dest='minTransactions', default=2, type=int, help='minimum transactions per block')
    parser.add_argument('-n', dest='maxTransactions', default=512, type=int, help='maximum transaction per block')
    parser.add_argument('--app', dest='runapp', default=False, help='run the flask app',
                        action='store_true')
    args = parser.parse_args()

    manager = Manager()
    manager.loadUsers()
    blockChain = Chain()
    version = '1.0a'

    if not args.runapp:
        if args.input == '':
            for i in range(args.blocks):
                if not (isPow2(args.minTransactions) and isPow2(args.maxTransactions)):
                    raise Exception("the maximum and minimum number of transactions must be power of 2")

                quantity = 2 ** (randint(int(log2(args.minTransactions)), int(log2(args.maxTransactions))))
                difficulty = int(randint(args.minDifficulty, args.maxDifficulty))
                transactions = []
                for j in range(quantity):
                    valor = randint(100, 100000) / 10
                    sender = manager.randomUser()
                    receiver = manager.randomUser()
                    message = sender.pubKeyAsAddress().decode() + receiver.pubKeyAsAddress().decode() + str(valor) + \
                        sender.pubKeyAsAddress().decode()
                    transactions.append(Transaction(sender.pubKeyAsAddress().decode(),
                                                    receiver.pubKeyAsAddress().decode(), valor,
                                                    sender.pubKeyAsAddress().decode(), sender.sign(message.encode()),
                                                    receiver.sign(message.encode())))

                blockChain.addBlock(Block(transactions, difficulty, version))

            blockChain.printAll()

            if args.output != '':
                blockChain.saveAsJson(args.output)

        else:
            blockChain.loadChain(args.input)
            blockChain.printAll()

    else:
        blockApp.run(host='localhost', port=8000)
