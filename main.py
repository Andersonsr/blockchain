from math import log2
from block import Block
from userManager import Manager
from transaction import Transaction
from chain import Chain
from miner import Miner
from random import randint
import argparse
from merkletree import isPow2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='minDifficulty', default=2, type=int, help='dificuldade minima')
    parser.add_argument('-m', dest='maxDifficulty', default=5, type=int, help='dificuldade maxima')
    parser.add_argument('-b', dest='blocks', default=10, type=int, help='numero de blocos')
    parser.add_argument('-o', dest='output', default='', type=str, help='nome do arquivo de saida')
    parser.add_argument('-i', dest='input', default='', type=str, help='nome do arquivo de entrada')
    parser.add_argument('-t', dest='minTransactions', default=2, type=int, help='minimo de transacoes por bloco')
    parser.add_argument('-n', dest='maxTransactions', default=512, type=int, help='maximo de transacoes por bloco')
    args = parser.parse_args()

    miner = Miner()
    manager = Manager()
    manager.loadUsers()
    blockChain = Chain()

    if args.input == '':
        for i in range(args.blocks):
            if not (isPow2(args.minTransactions) and isPow2(args.maxTransactions)):
                raise Exception("o numero maximo e minimo de transacoes precisa ser potencia de 2")

            quantity = 2**(randint(int(log2(args.minTransactions)), int(log2(args.maxTransactions))))
            difficulty = int(randint(args.minDifficulty, args.maxDifficulty))
            transactions = []
            for j in range(quantity):
                valor = randint(100, 100000)/10
                sender = manager.randomUser()
                receiver = manager.randomUser()
                message = sender.pubKeyPEM() + receiver.pubKeyPEM() + str(valor) + sender.pubKeyAsAddress().decode()
                transactions.append(Transaction(sender.pubKeyPEM(), receiver.pubKeyPEM(), valor,
                                                sender.pubKeyAsAddress(), sender.sign(message.encode()),
                                                receiver.sign(message.encode())))

            nonce, digest = miner.mine(transactions, difficulty)
            blockChain.addBlock(Block(transactions=transactions, nonce=nonce, hash=digest, difficulty=difficulty))

        blockChain.printAll()

        if args.output != '':
            blockChain.saveAsJson(args.output)

    else:
        blockChain.loadChain(args.input)
        blockChain.printAll()


