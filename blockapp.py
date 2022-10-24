import os
from flask import Flask
import json

blockApp = Flask('BlockApp')


@blockApp.route("/")
def homepage():
    return "<a href=\'blockchains/\'><p>read blockchain</p></a>" \
           "<p>create blockchain</p>"


@blockApp.route("/blockchains/")
def blockchains():
    content = ''
    for e in os.listdir('blocks/'):
        content += '<a href=\'/blockchains/{}\'><li>{}</li></a>'.format(e, e)
    return '<h1>blockchains</h1>' + '<ul>' + content + '</ul>'


@blockApp.route("/blockchains/<blockchain>/")
def chain(blockchain):
    blocks = os.listdir('blocks/{}/'.format(blockchain))
    content = '<h1>blockchain:{}</h1><ul>'.format(blockchain)
    for b in blocks:
        with open('blocks/{}/{}'.format(blockchain, b)) as file:
            data = json.load(file)
            content += '<a href=\'blockchains/{}/{}/\'><li>' \
                       '<p>hash:{}</p>' \
                       '<p>size:{}B</p>' \
                       '<p>difficulty:{}</p>' \
                       '<p>transactionNumber:{}</p>' \
                       '<p>merkleRoot:{}</p>' \
                       '<p>nonce:{}</p>' \
                       '</li></a>'.format(blockchain, data['hash'], data['hash'],
                                          data['size'],
                                          data['difficulty'],
                                          data['transactionsNumb'],
                                          data['merkleRoot'],
                                          data['nonce'])
    content += '</ul>'
    return content


@blockApp.route("/blockchains/<blockchain>/<block>/")
def block(blockchain, block):
    content = '<h1>blockchain:{}</h1>'.format(blockchain)
    content += '<h2>block:{}</h2><ul>'.format(block)
    with open('blocks/{}/{}.json'.format(blockchain, block)) as file:
        data = json.load(file)
        for t in data['transactions']:
            content += '<li>' \
                       '<p>sender:{}</p>' \
                       '<p>receiver:{}</p>' \
                       '<p>change:{}</p>' \
                       '<p>value:{}</p>' \
                       '<p>senderSignature:{}</p>' \
                       '<p>receiverSignature:{}</p>' \
                       '</li>'.format(t['sender'],
                                      t['receiver'],
                                      t['change'],
                                      t['value'],
                                      t['senderSignature'],
                                      t['receiverSignature'])
        content += '</ul>'
    return content
