from block import Block
from userManager import Manager
from transaction import Transaction
from chain import Chain
from miner import Miner
from random import randint
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='min', default=2, type=int, help='dificuldade minima')
    parser.add_argument('-m', dest='max', default=5, type=int, help='dificuldade maxima')
    parser.add_argument('-b', dest='blocos', default=10, type=int, help='numero de blocos')
    parser.add_argument('-o', dest='output', default='test', type=str, help='nome do arquivo de saida')
    parser.add_argument('-i', dest='input', default='', type=str, help='nome do arquivo de entrada')
    args = parser.parse_args()

    miner = Miner()
    manager = Manager()
    manager.loadUsers()
    blockChain = Chain()

    if args.input == '':
        for i in range(args.blocos):
            blockSize = int(2 ** randint(1, 9))
            difficulty = int(randint(args.min, args.max))
            transactions = []
            for j in range(blockSize):
                valor = randint(100, 100000)/10
                sender = manager.randomUser()
                receiver = manager.randomUser()
                message = sender.pubKeyPEM() + receiver.pubKeyPEM() + str(valor) # + sender.pubKeyAsAddress()
                transactions.append(Transaction(sender.pubKeyPEM(), receiver.pubKeyPEM(), valor,
                                                sender.pubKeyAsAddress(), sender.sign(message.encode()),
                                                receiver.sign(message.encode())))

            nonce, digest = miner.mine(transactions, difficulty)
            blockChain.addBlock(Block(transactions, nonce, digest, difficulty))

        blockChain.printAll()

        if args.output != '':
            blockChain.saveAsJson(args.output)




