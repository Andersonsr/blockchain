from block import transaction, block
from chain import chain
from miner import miner
from random import randint
from hashlib import sha256
import rsa
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dificuldadeMinima', default=2, type=int)
    parser.add_argument('-m', dest='dificuldadeMaxima', default=5, type=int)
    parser.add_argument('-b', dest='blocos', default=10, type=int)
    parser.add_argument('-o', dest='output', default='', type=str)
    parser.add_argument('-i', dest='input', default='', type=str)
    args = parser.parse_args()


    if args.input == '':
        blockchain = chain()
        miner1 = miner()
        for i in range(args.blocos):
            print('gerando bloco ' + str(i+1) + '...')
            transactions = []
            n = int(2**randint(1, 9))
            dificuldade = randint(args.dificuldadeMinima, args.dificuldadeMaxima)
            for j in range(n):
                origemPub, origemPriv = rsa.newkeys(512)
                destinoPub, destinoPriv = rsa.newkeys(512)
                troco = sha256(str(origemPub.n).encode()).hexdigest()
                valor = randint(1000, 10000)/10

                mensagem = (str(origemPub.n) + str(destinoPub.n) + troco + str(valor)).encode()
                signOrigem = rsa.sign(mensagem, origemPriv, 'SHA-1')
                signDestino = rsa.sign(mensagem, destinoPriv, 'SHA-1')

                transactions.append(transaction(origemPub, destinoPub, valor, troco, signOrigem, signDestino))

            nonce, digest = miner1.mine(transactions, dificuldade)
            b = block(transactions, nonce, digest, dificuldade)
            blockchain.addBlock(b)
            print('bloco {} gerado com sucesso! hash: {}\n'.format(i+1, digest))

        print('cadeia de blocos:')
        blockchain.printAll()

        if args.output != '':
            print('\nsalvando arquivo...')
            with open(args.output + '.json', 'w') as file:
                json.dump(blockchain.blocks, file)