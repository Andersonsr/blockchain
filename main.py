from block import block
from transaction import transaction
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

    randomSize = int(2**randint(1, 9))

