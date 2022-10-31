import os
from math import log2
from random import randint

from flask import Flask, request, redirect
import json

from block import Block
from chain import Chain
from transaction import Transaction
from userManager import Manager

blockApp = Flask('BlockApp')


@blockApp.route("/")
def homepage():
    return "<h1>Blockchain App</h1>" \
           "<a href=\'blockchains/\'><p>read blockchain</p></a>" \
           "<a href=\'/create/\'><p>create blockchain</p></a>"


@blockApp.route("/create/")
def creation():
    content = '<a href=\'/\'><h1>Blockchain App</h1></a>' \
              '<h2>Create Blockchain</h2>' \
              '<form action=\'/create/handle/\' method=\'post\'>' \
              '<label for=\'name\'>Blockchain name</label>' \
              '<input type=\'text\' id=\'name\' name=\'name\'>' \
              '<label for=\'min-block-size\'> Min transactions per block</label>' \
              '<select id=\'min-block-size\' name=\'min-block-size\'>'
    for i in range(1, 10):
        content += '<option value=\'{}\'>{}</option>'.format(2 ** i, 2 ** i)
    content += '</select>' \
               '<label for=\'max-block-size\'>Max transactions per block</label>' \
               '<select id=\'max-block-size\' name=\'max-block-size\'>'
    for i in range(1, 10):
        content += '<option value=\'{}\'>{}</option>'.format(2 ** i, 2 ** i)
    content += '</select>' \
               '<label for=\'number\'>blocks quantity</label>' \
               '<input type=\'number\' id=\'blocks\' name=\'blocks\'min=\'2\' max=\'100\'' \
               '<label for=\'min-difficulty\'>Min difficulty</label>' \
               '<input type=\'number\' id=\'min-difficulty\' name=\'min-difficulty\'min=\'1\' max=\'7\'>' \
               '<label for=\'max-difficulty\'>Max difficulty</label>' \
               '<input type=\'number\' id=\'max-difficulty\' name=\'max-difficulty\' min=\'1\' max=\'7\'>' \
               '<button type=\'submit\'>Submit</button>' \
               '</form>'

    return content


@blockApp.route("/create/handle/", methods=['GET', 'POST'])
def handleform():
    manager = Manager()
    manager.loadUsers()
    blockChain = Chain()
    version = '1.0a'
    tMin = int(request.form.get("min-block-size"))
    tMax = int(request.form.get("max-block-size"))
    diffMin = int(request.form.get("min-difficulty"))
    diffMax = int(request.form.get("max-difficulty"))
    chainName = request.form.get("name")
    blocks = int(request.form.get("blocks"))

    for i in range(blocks):
        quantity = 2 ** (randint(int(log2(tMin)), int(log2(tMax))))
        difficulty = int(randint(diffMin, diffMax))
        transactions = []
        for j in range(quantity):
            valor = randint(100, 100000) / 10
            sender = manager.randomUser()
            receiver = manager.randomUser()
            message = sender.pubKeyPEM() + receiver.pubKeyPEM() + str(valor) + sender.pubKeyAsAddress().decode()
            transactions.append(Transaction(sender.pubKeyPEM(), receiver.pubKeyPEM(), valor,
                                            sender.pubKeyAsAddress(), sender.sign(message.encode()),
                                            receiver.sign(message.encode())))

        blockChain.addBlock(Block(transactions, difficulty, version))
        blockChain.saveAsJson(chainName)

    return redirect('/blockchains/{}/'.format(chainName))


@blockApp.route("/blockchains/")
def blockchains():
    content = ''
    for e in os.listdir('blocks/'):
        content += '<a href=\'/blockchains/{}\'><li>{}</li></a>'.format(e, e)
    return '<a href=\'/\'><h1>Blockchain App</h1></a><h2>blockchains</h2>' + '<ul>' + content + '</ul>'


@blockApp.route("/blockchains/<blockchain>/")
def chain(blockchain):
    blocks = os.listdir('blocks/{}/'.format(blockchain))
    content = '<a href=\'/\'><h1>Blockchain App</h1></a>' \
              '<a href=\'/blockchains/{}\'><h2>blockchain:{}</h2></a><ul>'.format(blockchain, blockchain)
    chain = Chain(blockchain)
    chain.loadChain(blockchain)
    content += chain.toHTML()
    return content


@blockApp.route("/blockchains/<blockchain>/<block>/")
def block(blockchain, block):
    content = '<a href=\'/\'><h1>Blockchain App</h1></a>' \
              '<a href=\'/blockchains/{}/\'><h2>blockchain:{}</h2></a>'.format(blockchain, blockchain)
    content += '<h3>block:{}</h3>'.format(block)
    with open('blocks/{}/{}.json'.format(blockchain, block)) as file:
        data = json.load(file)
        counter = 0
        if data['previousHash'] != '0':
            content += '<a href=\'/blockchains/{}/{}/\'><p>previousBlock</p></a>'.format(blockchain,
                                                                                                 data['previousHash'])
        for t in data['transactions']:
            counter += 1
            content += '<li>' \
                       '<h4>Transaction {}</h4>' \
                       '<p>sender:{}</p>' \
                       '<p>receiver:{}</p>' \
                       '<p>change:{}</p>' \
                       '<p>value:{}</p>' \
                       '<p>senderSignature:{}</p>' \
                       '<p>receiverSignature:{}</p>' \
                       '</li>'.format(counter,
                                      t['sender'],
                                      t['receiver'],
                                      t['change'],
                                      t['value'],
                                      t['senderSignature'],
                                      t['receiverSignature'])
        content += '</ul>'
        if data['previousHash'] != '0':
            content += '<a href=\'/blockchains/{}/{}/\'><p>previousBlock</p></a>'.format(blockchain,
                                                                                         data['previousHash'])
    return content
